
import pytest
from Piece import Knight, Pawn, Rook, Bishop, Queen, King
from chess_engine import game_state
from enums import Player
from ai_engine import chess_ai


"""---------------------------------------------Test case 1 - Knight at (4,4) Board as start game---------------------------------------------------"""
# Define a fixture to create a Knight piece at (row, col) = (4, 4) for Player.PLAYER_1
@pytest.fixture
def knight():
    return Knight('n', 4, 4, Player.PLAYER_1)

# Define a fixture to create a game state as start game
@pytest.fixture
def game():
    return game_state()

# Use the fixtures in the test function for valid_piece_takes
def test1_get_valid_piece_takes(game, knight):
    # Call the function to test piece takes
    valid_takes = knight.get_valid_piece_takes(game)

    # Check if the result is correct
    expected_takes = [(6, 5), (6, 3)]
    assert valid_takes == expected_takes

# Use the fixtures in the test function for valid_peaceful_moves
def test1_get_valid_peaceful_moves(game, knight):
    # Call the function to test piece takes
    valid_takes = knight.get_valid_peaceful_moves(game)

    # Check if the result is correct
    expected_takes = [(2, 3), (2, 5), (3, 2), (3, 6), (5, 2), (5, 6)]
    assert valid_takes == expected_takes

# Use the fixtures in the integration test function for valid_piece_moves
def test1_get_valid_piece_moves(game, knight):
    # Call the function to test piece moves
    valid_moves = knight.get_valid_piece_moves(game)

    # Check if the result is correct
    expected_moves = [(2, 3), (2, 5), (3, 2), (3, 6), (5, 2), (5, 6), (6, 5), (6, 3)]
    assert valid_moves == expected_moves

"""---------------------------------------------Test case 2 - Knight at (3,3) Board as like this---------------------------------------------------
. . . . . . . .
. p . . . r . .
. . . b . . n .
. . . . k . . q
. . . K . . Q .
. . . B . . N .
. . P . . R . .
. . . . . . . .


"""
# Define a fixture to create a Knight piece at (row, col) = (3, 3) for Player.PLAYER_1
@pytest.fixture
def knight2():
    return Knight('n', 3, 3, Player.PLAYER_1)

# Define a fixture to create another manually modified game state
@pytest.fixture
def game2():
    game = game_state()

    for row in range(8):
        for col in range(8):
                game.board[row][col] = Player.EMPTY
    # Modify the game state by placing pieces in different positions
    game.board[1][1] = Pawn('p', 1, 1, Player.PLAYER_1)
    game.board[1][5] = Rook('r', 1, 5, Player.PLAYER_1)
    game.board[2][3] = Bishop('b', 2, 3, Player.PLAYER_1)
    game.board[2][6] = Knight('n', 2, 6, Player.PLAYER_1)
    game.board[3][4] = King('k', 3, 4, Player.PLAYER_1)
    game.board[3][7] = Queen('q', 3, 7, Player.PLAYER_1)

    game.board[6][0] = Pawn('p', 1, 4, Player.PLAYER_2)
    game.board[6][4] = Rook('r', 2, 4, Player.PLAYER_2)
    game.board[5][2] = Bishop('b', 3, 1, Player.PLAYER_2)
    game.board[5][5] = Knight('n', 5, 5, Player.PLAYER_2)
    game.board[4][3] = King('k', 4, 7, Player.PLAYER_2)
    game.board[4][6] = Queen('q', 0, 3, Player.PLAYER_2)

    return game

# Use the fixtures in the test function for valid_piece_takes
def test2_get_valid_piece_takes(game2, knight2):
    # Call the function to test piece takes
    valid_takes = knight2.get_valid_piece_takes(game2)

    # Check if the result is correct
    expected_takes = [(5, 2)]
    assert valid_takes == expected_takes

# Use the fixtures in the test function for valid_peaceful_moves
def test2_get_valid_peaceful_moves(game2, knight2):
    # Call the function to test piece takes
    valid_takes = knight2.get_valid_peaceful_moves(game2)

    # Check if the result is correct
    expected_takes = [(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 4)]
    assert valid_takes == expected_takes


# Use the fixtures in the integration test function for valid_piece_moves
def test2_get_valid_piece_moves(game2, knight2):
    # Call the function to test piece moves
    valid_moves = knight2.get_valid_piece_moves(game2)

    # Check if the result is correct
    expected_moves = [(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 4), (5, 2)]
    assert valid_moves == expected_moves

"""---------------------------------------------Test case 3 - Knight at (5,5) Board as like this---------------------------------------------------
. . . . . . . .
. p . . p r n .
. . . b . r . .
. . . . . K k .
. . . . n . . .
. . . . . . . .
. . . . Q b . .
. . . . . . . q
"""
# Define a fixture to create a Knight piece at (row, col) = (5, 6 for Player.PLAYER_1
@pytest.fixture
def knight3():
    return Knight('n', 5, 6, Player.PLAYER_1)

@pytest.fixture
def game3():
    game = game_state()

    for row in range(8):
        for col in range(8):
                game.board[row][col] = Player.EMPTY
    # Modify the game state by placing pieces in different positions
    game.board[1][1] = Pawn('p', 1, 1, Player.PLAYER_1)
    game.board[1][5] = Rook('r', 1, 5, Player.PLAYER_1)
    game.board[2][3] = Bishop('b', 2, 3, Player.PLAYER_1)
    game.board[4][4] = Knight('n', 4, 4, Player.PLAYER_1)
    game.board[3][5] = King('k', 3, 5, Player.PLAYER_1)
    game.board[7][7] = Queen('q', 7, 7, Player.PLAYER_1)

    game.board[1][4] = Pawn('p', 1, 4, Player.PLAYER_2)
    game.board[2][4] = Rook('r', 2, 4, Player.PLAYER_2)
    game.board[6][5] = Bishop('b', 6, 5, Player.PLAYER_2)
    game.board[1][6] = Knight('n', 1, 6, Player.PLAYER_2)
    game.board[3][6] = King('k', 3, 6, Player.PLAYER_2)
    game.board[6][4] = Queen('q', 6, 4, Player.PLAYER_2)

    return game
# Use the fixtures in the test function for valid_piece_takes
def test3_get_valid_piece_takes(game3, knight3):
    # Call the function to test piece takes
    valid_takes = knight3.get_valid_piece_takes(game3)

    # Check if the result is correct
    expected_takes = [(6, 4)]
    assert valid_takes == expected_takes

# Use the fixtures in the test function for valid_peaceful_moves
def test3_get_valid_peaceful_moves(game3, knight3):
    # Call the function to test piece takes
    valid_takes = knight3.get_valid_peaceful_moves(game3)

    # Check if the result is correct
    expected_takes = [(3, 7), (7, 5)]
    assert valid_takes == expected_takes

# Use the fixtures in the integration test function for valid_piece_moves
def test3_get_valid_piece_moves(game3, knight3):
    # Call the function to test piece moves
    valid_moves = knight3.get_valid_piece_moves(game3)

    # Check if the result is correct
    expected_moves = [(3, 7), (7, 5), (6, 4)]
    assert valid_moves == expected_moves


"""---------------------------------------------Integration Test case - Check Ai evaluate_scores--------------------------------------------------"""
@pytest.fixture
def ai():
    return chess_ai()

@pytest.fixture
def game4():
    game = game_state()

    for row in range(8):
        for col in range(8):
                game.board[row][col] = Player.EMPTY
    # Modify the game state by placing pieces in different positions
    game.board[1][1] = Pawn('p', 1, 1, Player.PLAYER_1)
    game.board[1][2] = Rook('r', 1, 2, Player.PLAYER_1)
    game.board[1][3] = Bishop('b', 1, 3, Player.PLAYER_1)
    game.board[1][4] = Knight('n', 1, 4, Player.PLAYER_1)
    game.board[1][5] = King('k', 1, 5, Player.PLAYER_1)
    game.board[1][6] = Queen('q', 1, 6, Player.PLAYER_1)

    game.board[2][1] = Pawn('p', 2, 1, Player.PLAYER_2)
    game.board[2][2] = Rook('r', 2, 2, Player.PLAYER_2)
    game.board[2][3] = Bishop('b', 2, 3, Player.PLAYER_2)
    game.board[2][4] = Knight('n', 2, 4, Player.PLAYER_2)
    game.board[2][5] = King('k', 2, 5, Player.PLAYER_2)
    game.board[1][6] = Queen('q', 2, 6, Player.PLAYER_2)

    return game


def test_evaluate_board(game4, ai):
    # Call the function to test piece moves
    evaluate_scores = ai.evaluate_board(game4, Player.PLAYER_1)

    # Check if the result is correct
    expected_scores = 100
    assert evaluate_scores == expected_scores


"""---------------------------------------------System Test case - Check Ai evaluate_scores--------------------------------------------------"""
def test_game(game):
    # Call the function to test piece moves - do the shorter checkmate way
    game.move_piece((1, 3), (3, 3), False)
    game.move_piece((6, 3), (4, 3), False)
    game.move_piece((0, 4), (4, 0), False)
    game.move_piece((6, 7), (4, 7), False)
    game.move_piece((0, 2), (3, 5), False)
    game.move_piece((4, 7), (3, 7), False)
    game.move_piece((4, 0), (6, 2), False)

    #got player was lost
    losser = game.checkmate_stalemate_checker()
    # Check if the result is correct - black player lost
    expected_losser = 1
    assert losser == expected_losser

