from treasure_hunt import is_valid_move, move_player, collect_item, check_trap, has_won


def sample():
    board = [list('P.G'), list('.#K'), list('TMV')]
    player = dict(row=0, col=0, moves=5, gold=0, keys=0, total_keys=1, score=0)
    return board, player


def test_valid():
    b, p = sample()
    assert is_valid_move(b, 0, 1)
    assert not is_valid_move(b, 1, 1)
    assert not is_valid_move(b, -1, 0)


def test_move():
    b, p = sample()
    assert move_player(b, p, 'RIGHT')
    assert (p['row'], p['col'], p['moves']) == (0, 1, 4)
    assert not move_player(b, p, 'DOWN')
    assert p['moves'] == 4


def test_collect():
    b, p = sample()
    p.update(row=0, col=2)
    assert collect_item(b, p) == 'G'
    assert p['gold'] == 1 and p['score'] == 100 and b[0][2] == '.'
    p.update(row=1, col=2)
    assert collect_item(b, p) == 'K'
    assert p['keys'] == 1 and b[1][2] == '.'
    p.update(row=2, col=1)
    assert collect_item(b, p) == 'M'
    assert p['moves'] == 13


def test_trap():
    b, p = sample()
    p.update(row=2, col=0)
    assert check_trap(b, p)
    assert p['moves'] == 2 and b[2][0] == '.'


def test_win():
    b, p = sample()
    p.update(row=2, col=2, gold=0, keys=1)
    assert has_won(b, p)  # Coins are optional.
    p['keys'] = 0
    assert not has_won(b, p)
    p['keys'] = 1
    p['col'] = 1
    assert not has_won(b, p)


def test_random_level_starts_are_empty_and_solvable():
    """Exercise the generator without opening a raylib graphics window."""
    import sys
    import types
    from unittest.mock import patch

    with patch.dict(sys.modules, {'pyray': types.ModuleType('pyray')}):
        import game
        for level in (1, 2, 5, 10):
            for _ in range(8):
                board, moves = game.new_level(level)
                player = game.make_player(level, moves, 0, board)
                row, col = player['row'], player['col']
                assert board[row][col] == 'P'
                assert sum(tile == 'P' for line in board for tile in line) == 1
                assert game.solvable(board, moves)


def test_new_level_helpers_and_move_bonus():
    """Test readable helper functions and the amount awarded by potions."""
    import sys
    import types
    from unittest.mock import patch
    with patch.dict(sys.modules, {'pyray': types.ModuleType('pyray')}):
        import game
        board = game.make_empty_board()
        assert len(board) == 8
        assert len(board[0]) == 8
        assert len(game.all_positions()) == 64
        board[2][3] = 'P'
        board[5][4] = 'V'
        assert game.find_tile(board, 'P') == (2, 3)
        assert game.find_tile(board, 'V') == (5, 4)
        assert len(game.neighbors(0, 0)) == 2
        assert len(game.neighbors(4, 4)) == 4


def test_one_turn_collects_a_coin_and_potion():
    """Verify the main turn function preserves item effects."""
    import sys
    import types
    from unittest.mock import patch
    with patch.dict(sys.modules, {'pyray': types.ModuleType('pyray')}):
        import game
        board = [list('PGM'), list('..K'), list('..V')]
        player = game.make_player(1, 10, 0, board)

        class NoAnimation:
            def burst(self, *args, **kwargs):
                pass
            def add_label(self, *args, **kwargs):
                pass

        effects = NoAnimation()
        game.rl.SKYBLUE = 'skyblue'
        game.rl.BLUE = 'blue'
        game.rl.WHITE = 'white'
        status, message = game.take_turn(board, player, 'RIGHT', effects, effects)
        assert status == 'PLAYING'
        assert player['gold'] == 1
        assert player['score'] == 100
        assert player['moves'] == 9
        assert board[0][1] == '.'
        status, message = game.take_turn(board, player, 'RIGHT', effects, effects)
        assert status == 'PLAYING'
        assert player['moves'] == 16  # One step (-1), then potion (+8).
        assert board[0][2] == '.'
