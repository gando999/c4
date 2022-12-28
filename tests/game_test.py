from c4.game import (
  ConnectFourGame,
  GAME_STATE_IN_PROGRESS,
  GAME_STATE_WINNER,
  PLAYER_1_TOKEN,
  PLAYER_2_TOKEN,
)

SYMBOL_1 = '1'
SYMBOL_2 = '2'

class TestConnectFourGameCollection:

  def test_basic_win_state_column(self):
    testee = ConnectFourGame('p1', 'p2', 4, 4)
    testee.update_grid(0, SYMBOL_1)
    assert GAME_STATE_IN_PROGRESS == testee.check_state()
    testee.update_grid(0, SYMBOL_1)
    testee.update_grid(0, SYMBOL_1)
    testee.update_grid(0, SYMBOL_1)
    assert GAME_STATE_WINNER == testee.check_state()

  def test_basic_win_state_row(self):
    testee = ConnectFourGame('p1', 'p2', 4, 4)
    testee.update_grid(0, SYMBOL_1)
    assert GAME_STATE_IN_PROGRESS == testee.check_state()
    testee.update_grid(1, SYMBOL_1)
    testee.update_grid(2, SYMBOL_1)
    assert GAME_STATE_IN_PROGRESS == testee.check_state()
    testee.update_grid(3, SYMBOL_1)
    assert GAME_STATE_WINNER == testee.check_state()

  def test_basic_win_state_diagonal(self):
    testee = ConnectFourGame('p1', 'p2', 4, 4)
    testee.update_grid(0, SYMBOL_1)
    assert GAME_STATE_IN_PROGRESS == testee.check_state()
    testee.update_grid(1, SYMBOL_2)
    testee.update_grid(1, SYMBOL_1)

    testee.update_grid(2, SYMBOL_2)
    testee.update_grid(2, SYMBOL_2)
    testee.update_grid(2, SYMBOL_1)

    testee.update_grid(3, SYMBOL_2)
    testee.update_grid(3, SYMBOL_2)
    testee.update_grid(3, SYMBOL_2)
    assert GAME_STATE_IN_PROGRESS == testee.check_state()
    testee.update_grid(3, SYMBOL_1)
    assert GAME_STATE_WINNER == testee.check_state()

  def test_switch_player(self):
    testee = ConnectFourGame('p1', 'p2', 4, 4)
    assert 'p1' == testee.current_player.name
    assert PLAYER_1_TOKEN == testee.current_player.token
    testee.switch_player()
    assert 'p2' == testee.current_player.name
    assert PLAYER_2_TOKEN == testee.current_player.token

  def test_out_of_range_token(self):
    testee = ConnectFourGame('p1', 'p2', 4, 4)
    assert -1 == testee.update_grid(100, SYMBOL_1)