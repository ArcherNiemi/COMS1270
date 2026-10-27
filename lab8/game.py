"""Goldhoarder's Treasure Hunt

Run: python game.py
Tests: python -m pytest -q

Start reading at main() near the bottom of this file. Each helper has one job:
  1. Make a level and its player
  2. Load and draw sprites
  3. Handle movement and pickups
  4. Animate sparkles, explosions, and floating numbers
  5. Draw the game window

DO NOT MAKE ANY CHANGES TO THIS FILE!

"""

import math
import random
from collections import deque
from pathlib import Path

import pyray as rl

from treasure_hunt import (
    POTION_BONUS,
    TRAP_PENALTY,
    check_trap,
    collect_item,
    has_won,
    move_player,
)

# ------------------------------ Game settings ------------------------------
BOARD_SIZE = 8
TILE_SIZE = 66
BOARD_LEFT = 36
BOARD_TOP = 100
WINDOW_WIDTH = 760
WINDOW_HEIGHT = 720
STARTING_MOVES = 25
LEVEL_BONUS = 500

# These names match the single-character letters stored in the board.
# . = empty, P = starting square, # = wall, V = vault/door,
# G = gold coin, K = key, M = move potion, T = trap.
SPRITE_FILES = {
    'floor': 'stone_floor.png',
    'wall': 'stone_wall.png',
    'player': 'floppsie_player.png',
    'coin': 'gold_coin.png',
    'key': 'gold_key.png',
    'boost': 'extra_moves_potion.png',
    'locked': 'locked_door.png',
    'unlocked': 'unlocked_door.png',
    'trap': 'trap.png',
}

ASSET_FOLDER = Path(__file__).resolve().parent


# ---------------------------- Level generation -----------------------------
def make_empty_board():
    """Build an 8-by-8 board full of empty floor tiles."""
    board = []
    for row in range(BOARD_SIZE):
        board_row = []
        for col in range(BOARD_SIZE):
            board_row.append('.')
        board.append(board_row)
    return board


def all_positions():
    """Return every (row, column) position on the board."""
    positions = []
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            positions.append((row, col))
    return positions


def find_tile(board, symbol):
    """Find the first square containing symbol, or return None."""
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == symbol:
                return (row, col)
    return None


def find_all_tiles(board, symbol):
    """Return a list of the coordinates of every matching tile."""
    positions = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == symbol:
                positions.append((row, col))
    return positions


def neighbors(row, col):
    """Return up to four neighboring positions (no diagonals)."""
    positions = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for change_row, change_col in directions:
        next_row = row + change_row
        next_col = col + change_col
        if 0 <= next_row < BOARD_SIZE and 0 <= next_col < BOARD_SIZE:
            positions.append((next_row, next_col))
    return positions


def level_settings(level):
    """Choose how many objects appear as the levels get harder."""
    walls = min(5 + (level - 1) // 2, 12)
    traps = min(2 + (level - 1) // 3, 5)
    potions = 3 if level < 4 else 2
    moves = max(18, STARTING_MOVES - (level - 1))
    keys = min(2 + (level - 1) // 3, 4)
    coins = min(4 + (level - 1) // 2, 8)
    return walls, traps, potions, moves, keys, coins


def place_random_tiles(board, positions, symbol, count):
    """Use available positions, so objects never overlap one another."""
    for unused in range(count):
        row, col = positions.pop()
        board[row][col] = symbol


def make_random_board(walls, traps, potions, keys, coins):
    """Randomize the player start and place every other tile afterward."""
    board = make_empty_board()
    positions = all_positions()
    random.shuffle(positions)
    place_random_tiles(board, positions, 'P', 1)
    place_random_tiles(board, positions, 'V', 1)
    place_random_tiles(board, positions, 'G', coins)
    place_random_tiles(board, positions, 'K', keys)
    place_random_tiles(board, positions, 'M', potions)
    place_random_tiles(board, positions, 'T', traps)
    place_random_tiles(board, positions, '#', walls)
    return board


def solvable(board, moves):
    """Check that at least one route collects all keys and reaches the vault.

    This is breadth-first search (BFS): try possible moves in a queue. Each
    search state remembers which one-use keys, potions, and traps were visited.
    A set of coordinates is easier to read than a compressed bit mask.

    For the same state, only the route with the MOST remaining moves matters.
    The `best_moves` dictionary prevents revisiting inferior routes forever.
    """
    starts = find_all_tiles(board, 'P')
    if len(starts) != 1:
        return False

    all_keys = frozenset(find_all_tiles(board, 'K'))
    start_row, start_col = starts[0]
    empty = frozenset()
    start = (start_row, start_col, empty, empty, empty, moves)
    queue = deque()
    queue.append(start)
    best_moves = {}
    best_moves[start[:5]] = moves

    while len(queue) > 0:
        row, col, found_keys, used_potions, used_traps, remaining = queue.popleft()
        if board[row][col] == 'V' and found_keys == all_keys:
            return True
        if remaining <= 0:
            continue

        for next_row, next_col in neighbors(row, col):
            tile = board[next_row][next_col]
            if tile == '#':
                continue

            position = (next_row, next_col)
            next_keys = found_keys
            next_potions = used_potions
            next_traps = used_traps
            next_moves = remaining - 1

            if tile == 'K':
                next_keys = found_keys.union([position])
            elif tile == 'M' and position not in used_potions:
                next_moves += POTION_BONUS
                next_potions = used_potions.union([position])
            elif tile == 'T' and position not in used_traps:
                next_moves -= TRAP_PENALTY
                next_traps = used_traps.union([position])

            if next_moves < 0:
                continue

            state = (next_row, next_col, next_keys, next_potions, next_traps)
            if state in best_moves and best_moves[state] >= next_moves:
                continue

            best_moves[state] = next_moves
            queue.append((next_row, next_col, next_keys,
                          next_potions, next_traps, next_moves))

    return False


def make_fallback_board(keys, coins):
    """Build a simple solvable layout if random attempts all fail."""
    board = make_empty_board()
    board[0][0] = 'P'
    for index in range(keys):
        board[0][index + 1] = 'K'
    board[0][keys + 1] = 'V'
    coin_positions = [(1, 0), (1, 1), (1, 2), (2, 0),
                      (2, 1), (2, 2), (3, 0), (3, 1)]
    for index in range(coins):
        row, col = coin_positions[index]
        board[row][col] = 'G'
    board[1][5] = 'M'
    # Rotate/reflect the layout so the starting position varies.
    if random.choice([True, False]):
        rotated = make_empty_board()
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                rotated[col][row] = board[row][col]
        board = rotated
    if random.choice([True, False]):
        board.reverse()
    if random.choice([True, False]):
        for row in board:
            row.reverse()
    return board


def new_level(level):
    """Return (board, moves), ensuring the board can actually be beaten."""
    walls, traps, potions, moves, keys, coins = level_settings(level)
    for attempt in range(250):
        board = make_random_board(walls, traps, potions, keys, coins)
        if solvable(board, moves):
            return board, moves
    return make_fallback_board(keys, coins), moves


def make_player(level, moves, score, board):
    """Create the player dictionary at the randomly chosen P square."""
    starts = find_all_tiles(board, 'P')
    if len(starts) != 1:
        raise ValueError('A level must contain exactly one player start (P).')
    row, col = starts[0]
    return {
        'row': row,
        'col': col,
        'moves': moves,
        'gold': 0,
        'keys': 0,
        'total_keys': len(find_all_tiles(board, 'K')),
        'level': level,
        'score': score,
    }


# ------------------------------ Sprite drawing -----------------------------
def load_sprites():
    """Load all PNGs from the same folder as this Python file."""
    sprites = {}
    for name in SPRITE_FILES:
        filename = SPRITE_FILES[name]
        path = ASSET_FOLDER / filename
        if not path.is_file():
            raise FileNotFoundError('Missing game sprite: ' + str(path))
        texture = rl.load_texture(str(path))
        rl.set_texture_filter(texture, rl.TEXTURE_FILTER_POINT)
        sprites[name] = texture
    return sprites


def unload_sprites(sprites):
    """Release graphics memory when the game window closes."""
    for name in sprites:
        rl.unload_texture(sprites[name])


def draw_sprite(texture, x, y):
    """Draw a PNG scaled to one board square."""
    source = rl.Rectangle(0, 0, texture.width, texture.height)
    destination = rl.Rectangle(x, y, TILE_SIZE, TILE_SIZE)
    rl.draw_texture_pro(texture, source, destination, rl.Vector2(0, 0), 0, rl.WHITE)


def tile_center(row, col):
    """Convert board coordinates to the pixel center of a tile."""
    x = BOARD_LEFT + (col + 0.5) * TILE_SIZE
    y = BOARD_TOP + (row + 0.5) * TILE_SIZE
    return x, y


def draw_board(board, player, sprites):
    """Draw floor first, then objects, then Floppsie on top."""
    door_is_open = player['keys'] == player['total_keys']
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            x = BOARD_LEFT + col * TILE_SIZE
            y = BOARD_TOP + row * TILE_SIZE
            draw_sprite(sprites['floor'], x, y)
            tile = board[row][col]
            sprite_name = None
            if tile == '#':
                sprite_name = 'wall'
            elif tile == 'G':
                sprite_name = 'coin'
            elif tile == 'K':
                sprite_name = 'key'
            elif tile == 'M':
                sprite_name = 'boost'
            elif tile == 'T':
                sprite_name = 'trap'
            elif tile == 'V':
                sprite_name = 'unlocked' if door_is_open else 'locked'
            if sprite_name is not None:
                draw_sprite(sprites[sprite_name], x, y)

    player_x = BOARD_LEFT + player['col'] * TILE_SIZE
    player_y = BOARD_TOP + player['row'] * TILE_SIZE
    draw_sprite(sprites['player'], player_x, player_y)


def draw_centered_text(message, center_x, y, size, color):
    """Center a message by measuring its width before drawing."""
    width = rl.measure_text(message, size)
    rl.draw_text(message, int(center_x - width / 2), y, size, color)


# ------------------------------- Animations --------------------------------
class Sparkles:
    """A collection of little animated four-point stars."""

    def __init__(self):
        self.particles = []
        self.ambient_timer = 0.0

    def burst(self, x, y, count=18, palette=None, speed=100):
        """Create stars flying outward from a given screen position."""
        if palette is None:
            palette = [rl.GOLD, rl.YELLOW, rl.WHITE]
        for index in range(count):
            angle = random.uniform(0, math.tau)
            velocity = random.uniform(speed * 0.25, speed)
            lifetime = random.uniform(0.4, 0.95)
            particle = {
                'x': x + random.uniform(-7, 7),
                'y': y + random.uniform(-7, 7),
                'vx': math.cos(angle) * velocity,
                'vy': math.sin(angle) * velocity - 18,
                'life': lifetime,
                'max_life': lifetime,
                'size': random.uniform(1.7, 4.0),
                'color': random.choice(palette),
            }
            self.particles.append(particle)

    def update(self, dt):
        """Move each star, shorten its lifetime, and remove expired stars."""
        dt = min(dt, 0.05)
        remaining_particles = []
        for particle in self.particles:
            particle['life'] -= dt
            if particle['life'] > 0:
                particle['x'] += particle['vx'] * dt
                particle['y'] += particle['vy'] * dt
                particle['vy'] += 55 * dt
                remaining_particles.append(particle)
        self.particles = remaining_particles

    def draw(self):
        """Draw each star as crossing lines and a tiny center circle."""
        for particle in self.particles:
            fade = particle['life'] / particle['max_life']
            color = rl.fade(particle['color'], fade)
            x = particle['x']
            y = particle['y']
            radius = particle['size'] * (0.6 + fade * 0.4)
            thickness = max(1, radius * 0.6)
            rl.draw_line_ex(rl.Vector2(x - radius * 1.7, y),
                            rl.Vector2(x + radius * 1.7, y), thickness, color)
            rl.draw_line_ex(rl.Vector2(x, y - radius * 1.7),
                            rl.Vector2(x, y + radius * 1.7), thickness, color)
            rl.draw_circle_v(rl.Vector2(x, y), radius * 0.6, color)


class Explosions:
    """Red trap blasts, expanding shockwaves, and floating move numbers."""

    def __init__(self):
        self.fragments = []
        self.rings = []
        self.labels = []

    def burst(self, x, y, count=32, scale=1.0, show_loss=False):
        """Create a predominantly red cartoon explosion at (x, y)."""
        palette = [rl.RED, rl.RED, rl.RED, rl.MAROON, rl.MAROON,
                   rl.Color(255, 45, 65, 255), rl.Color(230, 20, 45, 255),
                   rl.ORANGE, rl.GOLD]
        for index in range(count):
            angle = random.uniform(0, math.tau)
            speed = random.uniform(65, 205) * scale
            lifetime = random.uniform(0.35, 0.78)
            self.fragments.append({
                'x': x + random.uniform(-4, 4),
                'y': y + random.uniform(-4, 4),
                'vx': math.cos(angle) * speed,
                'vy': math.sin(angle) * speed,
                'life': lifetime,
                'max_life': lifetime,
                'radius': random.uniform(2.2, 5.3) * scale,
                'color': random.choice(palette),
            })
        self.rings.append({
            'x': x, 'y': y, 'age': 0.0,
            'duration': 0.38, 'max_radius': 34 * scale,
        })
        if show_loss:
            self.add_label(x, y, '-' + str(TRAP_PENALTY), rl.RED)

    def add_label(self, x, y, message, color):
        """Display a number that rises and fades beside the MOVES counter."""
        self.labels.append({
            'x': x, 'y': y - 17, 'age': 0.0,
            'duration': 1.0, 'text': str(message), 'color': color,
        })

    def update(self, dt):
        """Advance the explosion animation and remove finished elements."""
        dt = min(dt, 0.05)
        active_fragments = []
        for fragment in self.fragments:
            fragment['life'] -= dt
            if fragment['life'] > 0:
                fragment['x'] += fragment['vx'] * dt
                fragment['y'] += fragment['vy'] * dt
                fragment['vx'] *= max(0, 1 - 2.0 * dt)
                fragment['vy'] += 110 * dt
                active_fragments.append(fragment)
        self.fragments = active_fragments

        active_rings = []
        for ring in self.rings:
            ring['age'] += dt
            if ring['age'] < ring['duration']:
                active_rings.append(ring)
        self.rings = active_rings

        active_labels = []
        for label in self.labels:
            label['age'] += dt
            if label['age'] < label['duration']:
                active_labels.append(label)
        self.labels = active_labels

    def draw(self):
        """Draw shockwaves, fragments, and floating red/blue numbers."""
        for ring in self.rings:
            progress = ring['age'] / ring['duration']
            radius = ring['max_radius'] * progress
            color = rl.fade(rl.RED, 1 - progress)
            rl.draw_ring(rl.Vector2(ring['x'], ring['y']),
                         max(0, radius - 3), radius + 1, 0, 360, 36, color)

        for fragment in self.fragments:
            fade = fragment['life'] / fragment['max_life']
            radius = fragment['radius'] * (0.5 + 0.5 * fade)
            color = rl.fade(fragment['color'], fade)
            rl.draw_circle_v(rl.Vector2(fragment['x'], fragment['y']), radius, color)

        for label in self.labels:
            progress = label['age'] / label['duration']
            font_size = 25
            width = rl.measure_text(label['text'], font_size)
            x = int(label['x'] - width / 2)
            y = int(label['y'] - 23 * progress)
            shadow = rl.fade(rl.DARKBROWN, 1 - progress)
            foreground = rl.fade(label['color'], 1 - progress)
            rl.draw_text(label['text'], x + 1, y + 1, font_size, shadow)
            rl.draw_text(label['text'], x, y, font_size, foreground)


def update_door_sparkles(board, player, sparkles, dt, status):
    """Keep a gentle twinkle around the vault once all keys are collected."""
    door_open = player['keys'] == player['total_keys']
    if status != 'PLAYING' or not door_open:
        sparkles.ambient_timer = 0.0
        return

    sparkles.ambient_timer += dt
    if sparkles.ambient_timer < 0.15:
        return
    sparkles.ambient_timer = 0.0
    vault = find_tile(board, 'V')
    if vault is not None:
        x, y = tile_center(vault[0], vault[1])
        x += random.uniform(-22, 22)
        y += random.uniform(-22, 22)
        sparkles.burst(x, y, 3, speed=35)


# ------------------------------- Game events -------------------------------
def read_direction():
    """Read arrow keys and return a direction string or None."""
    if rl.is_key_pressed(rl.KEY_UP):
        return 'UP'
    if rl.is_key_pressed(rl.KEY_DOWN):
        return 'DOWN'
    if rl.is_key_pressed(rl.KEY_LEFT):
        return 'LEFT'
    if rl.is_key_pressed(rl.KEY_RIGHT):
        return 'RIGHT'
    return None


def celebrate_pickup(board, player, item, old_moves, old_keys, sparkles, explosions):
    """Play the appropriate sparkles and HUD effects for a collected item."""
    if item is None:
        return

    x, y = tile_center(player['row'], player['col'])
    if item == 'K':
        sparkles.burst(x, y, 22)
    else:
        sparkles.burst(x, y, 17)

    if item == 'M':
        sparkles.burst(668, 178, 24,
                       [rl.SKYBLUE, rl.BLUE, rl.WHITE], speed=85)
        bonus = player['moves'] - old_moves
        explosions.add_label(684, 178, '+' + str(bonus), rl.BLUE)

    if item == 'K' and old_keys < player['total_keys']:
        if player['keys'] == player['total_keys']:
            vault = find_tile(board, 'V')
            if vault is not None:
                door_x, door_y = tile_center(vault[0], vault[1])
                sparkles.burst(door_x, door_y, 75, speed=135)


def celebrate_trap(player, explosions):
    """Show a red blast on the trap tile and another at the MOVES counter."""
    x, y = tile_center(player['row'], player['col'])
    explosions.burst(x, y, count=38, scale=1.0)
    explosions.burst(684, 178, count=29, scale=0.72, show_loss=True)


def message_for_item(item):
    """Choose a short explanation for the bottom of the screen."""
    if item == 'G':
        return 'Gold collected!'
    if item == 'K':
        return 'Key collected! Find all keys to exit.'
    if item == 'M':
        return '+' + str(POTION_BONUS) + ' moves!'
    return 'Watch your step!'


def take_turn(board, player, direction, sparkles, explosions):
    """Move once, collect any item, check for traps, then check for victory.

    Return (new_status, message). Keeping these steps together makes the order
    of events obvious: moving costs 1, then potions/traps change moves.
    """
    if not move_player(board, player, direction):
        return 'PLAYING', None

    old_keys = player['keys']
    old_moves = player['moves']
    item = collect_item(board, player)
    celebrate_pickup(board, player, item, old_moves, old_keys, sparkles, explosions)
    message = message_for_item(item)

    if check_trap(board, player):
        celebrate_trap(player, explosions)
        message = 'Trap! Lost ' + str(TRAP_PENALTY) + ' extra moves.'

    if has_won(board, player):
        player['score'] += LEVEL_BONUS
        return 'LEVEL_COMPLETE', 'Vault opened! Press ENTER for the next level.'
    if player['moves'] <= 0:
        return 'GAME_OVER', 'Out of moves! Press ENTER for a new run.'
    return 'PLAYING', message


def start_level(level, score):
    """Build a new board and player while keeping the score from earlier levels."""
    board, moves = new_level(level)
    player = make_player(level, moves, score, board)
    return board, player


# ------------------------------- Screen layout -----------------------------
def draw_hud(player, level):
    """Draw the level, moves, coins, keys, and score at the right."""
    x = 590
    rl.draw_text('LEVEL  ' + str(level), x, 115, 23, rl.DARKGRAY)
    move_color = rl.MAROON if player['moves'] <= 5 else rl.DARKGRAY
    rl.draw_text('MOVES  ' + str(player['moves']), x, 166, 22, move_color)
    rl.draw_text('COINS  ' + str(player['gold']), x, 217, 22, rl.DARKGRAY)
    keys_text = str(player['keys']) + '/' + str(player['total_keys'])
    rl.draw_text('KEYS   ' + keys_text, x, 268, 22, rl.DARKGRAY)
    rl.draw_text('SCORE  ' + str(player['score']), x, 319, 22, rl.DARKGRAY)


def draw_end_panel(status, player, level):
    """Draw a centered overlay when a level ends or Floppsie runs out of moves."""
    if status == 'PLAYING':
        return
    panel_x = 90
    panel_y = 245
    panel_width = 570
    panel_height = 190
    center_x = panel_x + panel_width / 2
    rl.draw_rectangle(panel_x, panel_y, panel_width, panel_height,
                      rl.Color(255, 255, 255, 245))
    rl.draw_rectangle_lines(panel_x, panel_y, panel_width, panel_height, rl.DARKGRAY)

    if status == 'LEVEL_COMPLETE':
        draw_centered_text('LEVEL COMPLETE!', center_x, 277, 38, rl.DARKGREEN)
        draw_centered_text('Press ENTER to play the next level',
                           center_x, 366, 19, rl.DARKGRAY)
    else:
        draw_centered_text('GAME OVER', center_x, 277, 38, rl.MAROON)
        summary = 'Final score: ' + str(player['score'])
        summary += '   Level reached: ' + str(level)
        draw_centered_text(summary, center_x, 341, 20, rl.DARKGRAY)
        draw_centered_text('Press ENTER to restart at Level 1',
                           center_x, 385, 19, rl.DARKGRAY)


def draw_frame(board, player, level, message, status, sprites, sparkles, explosions):
    """Draw one complete frame in the correct layering order."""
    rl.begin_drawing()
    rl.clear_background(rl.Color(250, 248, 241, 255))
    rl.draw_text("GOLDHOARDER'S TREASURE HUNT", 35, 25, 28, rl.DARKBROWN)
    draw_board(board, player, sprites)
    sparkles.draw()
    draw_hud(player, level)
    # HUD explosions must appear over the HUD numbers.
    explosions.draw()
    rl.draw_text('Arrow keys: move', 35, 651, 19, rl.GRAY)
    rl.draw_text(message, 35, 680, 17, rl.DARKGRAY)
    draw_end_panel(status, player, level)
    rl.end_drawing()


# ------------------------------- Main program ------------------------------
def main():
    """Set up the game and repeat input → update → draw until the window closes."""
    rl.init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Goldhoarder's Treasure Hunt")
    rl.set_target_fps(60)
    sprites = {}
    try:
        sprites = load_sprites()
        level = 1
        board, player = start_level(level, score=0)
        sparkles = Sparkles()
        explosions = Explosions()
        status = 'PLAYING'
        message = 'Collect every key to exit; coins are bonus points!'

        while not rl.window_should_close():
            dt = rl.get_frame_time()
            sparkles.update(dt)
            explosions.update(dt)
            update_door_sparkles(board, player, sparkles, dt, status)

            if status == 'PLAYING':
                direction = read_direction()
                if direction is not None:
                    status, new_message = take_turn(
                        board, player, direction, sparkles, explosions)
                    if new_message is not None:
                        message = new_message

            elif rl.is_key_pressed(rl.KEY_ENTER):
                # ENTER continues after winning or restarts after losing.
                if status == 'LEVEL_COMPLETE':
                    level += 1
                    score = player['score']
                    message = 'New level! Find every key; coins earn points.'
                else:
                    level = 1
                    score = 0
                    message = 'New run! Good luck, Floppsie.'
                board, player = start_level(level, score)
                sparkles = Sparkles()
                explosions = Explosions()
                status = 'PLAYING'

            draw_frame(board, player, level, message, status,
                       sprites, sparkles, explosions)
    finally:
        unload_sprites(sprites)
        rl.close_window()


if __name__ == '__main__':
    main()
