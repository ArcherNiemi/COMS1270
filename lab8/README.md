# Goldhoarder's Treasure Hunt — Classroom-Friendly Edition

This is the same 8 × 8 sprite-based Python/raylib game, refactored for students learning programming. The goal is **clarity**, not minimizing the number of lines of code.

## Getting started

1. Keep `game.py`, `treasure_hunt.py`, and all nine `.png` files in the same folder.
2. Install the dependency: `python -m pip install -r requirements.txt`
3. Run the game: `python game.py`
4. Run automated tests: `python -m pytest -q`

The project uses `pyray` (Python's raylib bindings). The graphics window requires a desktop environment.

## Controls and rules

Use the **arrow keys** to move Floppsie. Walking into a wall or off the board does nothing and does not cost a move. Each successful step costs one move. Collect **all keys** to unlock the door, then step on the door to finish the level. Coins are optional and worth 100 points each. Potions give **8 moves**. Traps cost **3 additional moves**, on top of the step used to enter the trap. Finishing a level gives 500 bonus points. Press **Enter** to continue to the next level, or to restart from Level 1 after Game Over.

The player starts on a randomly chosen unoccupied square, and generated boards are checked to make sure a winning path exists within the move budget.

## Suggested reading order for students

1. **`treasure_hunt.py`** — the five core rules: `is_valid_move`, `move_player`, `collect_item`, `check_trap`, and `has_won`. These are ordinary Python functions with no graphics dependency.
2. **`game.py`: `main()`** — the central game loop: read input, update the game, draw a frame. Start here to understand how the pieces fit together.
3. **`game.py`: `take_turn()`** — shows the exact order of a move: step, collect, check trap, check win or loss.
4. **`game.py`: `draw_board()` and `draw_hud()`** — explains how the board and scores appear on screen.
5. **`game.py`: `new_level()` and `solvable()`** — the more advanced random level generation and breadth-first search.
6. **`Sparkles` and `Explosions`** — optional enrichment material showing frame-based animation with positions, velocities, and lifetimes.

## Board letters

| Letter | Meaning |
|---|---|
| `.` | Empty floor |
| `P` | Floppsie's starting square |
| `#` | Wall |
| `G` | Gold coin |
| `K` | Key |
| `M` | Move-increase potion |
| `T` | Bear trap |
| `V` | Vault / exit door |

The board is a **list of lists of strings**. For example, `board[2][3]` is the square in row 2, column 3. Row and column indices start at zero.

## Artwork and animation

All nine 64 × 64 PNG sprites are included. Coins, keys, and potions produce sparkles when collected. The door sparkles when all keys are found. Potions show a floating **blue +8** near the MOVES counter. Traps trigger red explosions on the board and at the MOVES counter, along with a floating **red -3**. No extra artwork or packages are required for these effects.
