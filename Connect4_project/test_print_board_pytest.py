from main import Connect4


def test_print_board_output(capsys):
    game = Connect4()

    game.print_board()

    captured = capsys.readouterr()

    assert "Current Board:" in captured.out
    assert "1 2 3 4 5 6 7" in captured.out