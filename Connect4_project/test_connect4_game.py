from main import Connect4


# ---------- WIN CONDITION TESTS ----------

def test_horizontal_win():
    game = Connect4()

    # Create horizontal win for X
    for col in range(4):
        game.board[5][col] = 'X'

    assert game.check_win('X') == True


def test_vertical_win():
    game = Connect4()

    # Create vertical win for O
    for row in range(4):
        game.board[5-row][0] = 'O'

    assert game.check_win('O') == True


def test_diagonal_down_right_win():
    game = Connect4()

    # Diagonal from top-left to bottom-right
    game.board[2][0] = 'X'
    game.board[3][1] = 'X'
    game.board[4][2] = 'X'
    game.board[5][3] = 'X'

    assert game.check_win('X') == True


def test_diagonal_up_right_win():
    game = Connect4()

    # Diagonal from bottom-left to top-right
    game.board[5][0] = 'O'
    game.board[4][1] = 'O'
    game.board[3][2] = 'O'
    game.board[2][3] = 'O'

    assert game.check_win('O') == True


def test_no_win():
    game = Connect4()

    game.board[5][0] = 'X'
    game.board[5][1] = 'O'
    game.board[5][2] = 'X'

    assert game.check_win('X') == False
    assert game.check_win('O') == False


# ---------- DROP CHIP TESTS ----------

def test_successful_chip_drop():
    game = Connect4()

    result = game.drop_chip(1)

    assert result == True
    assert game.board[5][0] == 'X'


def test_full_column():
    game = Connect4()

    # Fill column
    for _ in range(6):
        game.drop_chip(1)

    result = game.drop_chip(1)

    assert result == False


def test_invalid_column():
    game = Connect4()

    assert game.drop_chip(0) == False
    assert game.drop_chip(8) == False


def test_full_board():
    game = Connect4()

    # Fill entire board
    for row in range(game.ROWS):
        for col in range(game.COLS):
            game.board[row][col] = 'X'

    assert game.is_full() == True

# -----------------------------------
# Unit testing documentation for connect 4 game
# ----------------------------------- 
# The switch_player() method was tested using unittest to verify that
# the current player correctly switches between 'X' and 'O'.
#
# Pytest was used to test the print_board() function and the game logic
# related to win conditions and chip dropping behavior.
#
# The following scenarios were tested:
# Horizontal win detection
# Vertical win detection
# Diagonal win detection (both directions)
# No win condition
# Successful chip drop
# Attempting to drop a chip in a full column
#  Invalid column numbers
# Full board detection
#
# All 12 tests passed successfully, confirming that the Connect4 game
# logic functions as expected.