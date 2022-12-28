from c4.grid import (
  GridState,
  Column,
  Grid,
  EMPTY_SLOT
)

SYMBOL_1 = '1'
SYMBOL_2 = '2'

class TestGridStateCollection:

  def test_empty_grid_state(self):
    testee = GridState()
    testee.add_states([EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT])
    assert testee.is_winner() is False

  def test_non_winning_state_single_symbol(self):
    testee = GridState()
    testee.add_states([
      EMPTY_SLOT,
      EMPTY_SLOT,
      SYMBOL_1,
      SYMBOL_1,
      SYMBOL_1,
    ])
    assert testee.is_winner() is False

  def test_non_winning_state_right_count_non_consecutive(self):
    testee = GridState()
    testee.add_states([
      SYMBOL_2,
      SYMBOL_1,
      SYMBOL_2,
      SYMBOL_1,
      SYMBOL_2,
      SYMBOL_1,
      SYMBOL_2,
      SYMBOL_1,
    ])
    assert testee.is_winner() is False

  def test_winning_state_single_symbol(self):
    testee = GridState()
    testee.add_states([
      EMPTY_SLOT,
      EMPTY_SLOT,
      SYMBOL_1,
      SYMBOL_1,
      SYMBOL_1,
      SYMBOL_1,
    ])
    assert testee.is_winner() is True

  def test_winning_state_mixed_symbol_with_empty(self):
    testee = GridState()
    testee.add_states([
      SYMBOL_2,
      EMPTY_SLOT,
      SYMBOL_1,
      SYMBOL_1,
      SYMBOL_1,
      SYMBOL_1,
    ])
    assert testee.is_winner() is True

  def test_winning_state_mixed_symbol_starts_empty(self):
    testee = GridState()
    testee.add_states([
      EMPTY_SLOT,
      SYMBOL_2,
      SYMBOL_1,
      SYMBOL_1,
      SYMBOL_1,
      SYMBOL_1,
    ])
    assert testee.is_winner() is True

  def test_winning_state_mixed_symbol(self):
    testee = GridState()
    testee.add_states([
      SYMBOL_2,
      SYMBOL_2,
      SYMBOL_1,
      SYMBOL_1,
      SYMBOL_1,
      SYMBOL_1,
    ])
    assert testee.is_winner() is True

  def test_winning_state_mixed_symbol_two_wins(self):
    testee = GridState()
    testee.add_states([
      SYMBOL_2,
      SYMBOL_2,
      SYMBOL_2,
      SYMBOL_2,
      SYMBOL_1,
      SYMBOL_1,
      SYMBOL_1,
      SYMBOL_1,
    ])
    assert testee.is_winner() is True

  def test_winning_state_mixed_symbol_one_win_one_close(self):
    testee = GridState()
    testee.add_states([
      SYMBOL_2,
      SYMBOL_2,
      SYMBOL_2,
      EMPTY_SLOT,
      SYMBOL_1,
      SYMBOL_1,
      SYMBOL_1,
      SYMBOL_1,
    ])
    assert testee.is_winner() is True

class TestColumnCollection:

  def test_column_create_with_empty_slots(self):
    testee = Column(6)
    assert testee.height() == 6
    assert True == testee.has_empty_slots()

  def test_last_empty_slot_when_empty(self):
    testee = Column(6)
    assert testee.last_empty_slot() == 5 # zero indexed

  def test_add_token_fills_column(self):
    testee = Column(6)
    testee.add(SYMBOL_1)
    assert testee.last_empty_slot() == 4 # zero indexed

  def test_completely_filled_column(self):
    testee = Column(6)
    testee.add(SYMBOL_1)
    testee.add(SYMBOL_1)
    testee.add(SYMBOL_1)
    testee.add(SYMBOL_1)
    testee.add(SYMBOL_1)
    assert True == testee.has_empty_slots()
    testee.add(SYMBOL_1)
    assert testee.last_empty_slot() == -1
    assert False == testee.has_empty_slots()

class TestGridCollection:

  def test_default_row_count(self):
    testee = Grid()
    assert 6 == testee.row_count()

  def test_arg_level_row_count(self):
    testee = Grid(2, 2)
    assert 2 == testee.row_count()

  def test_default_column_count(self):
    testee = Grid()
    assert 7 == testee.column_count()

  def test_arg_level_column_count(self):
    testee = Grid(2, 2)
    assert 2 == testee.column_count()

  def test_state_as_columns(self):
    testee = Grid(2, 2)
    testee.add_counter(0, SYMBOL_1)
    testee.add_counter(0, SYMBOL_1)
    testee.add_counter(1, SYMBOL_2)
    testee.add_counter(1, SYMBOL_2)
    expected = [[SYMBOL_1, SYMBOL_1], [SYMBOL_2, SYMBOL_2]]
    assert expected == list(x.states for x in testee.state_as_columns())

  def test_state_as_rows(self):
    testee = Grid(2, 2)
    testee.add_counter(0, SYMBOL_1)
    testee.add_counter(0, SYMBOL_1)
    testee.add_counter(1, SYMBOL_2)
    testee.add_counter(1, SYMBOL_2)
    expected = [[SYMBOL_1, SYMBOL_2], [SYMBOL_1, SYMBOL_2]]
    assert expected == list(x.states for x in testee.state_as_rows())

  def test_state_as_simple_diagonals(self):
    testee = Grid(2, 2)
    testee.add_counter(0, SYMBOL_1)
    testee.add_counter(0, SYMBOL_1)
    testee.add_counter(1, SYMBOL_2)
    testee.add_counter(1, SYMBOL_2)
    expected = [
        [SYMBOL_1, SYMBOL_1, SYMBOL_2], 
        [SYMBOL_2, SYMBOL_2, SYMBOL_1],
        [SYMBOL_1],
        [SYMBOL_2],
    ]
    assert expected == list(x.states for x in testee.state_as_diagonals())

  def test_state_as_diagonals(self):
    testee = Grid(3, 3)
    testee.add_counter(0, SYMBOL_1)
    testee.add_counter(0, SYMBOL_1)
    testee.add_counter(0, SYMBOL_1)
    testee.add_counter(1, SYMBOL_2)
    testee.add_counter(1, SYMBOL_2)
    testee.add_counter(1, SYMBOL_2)
    expected = [
        [SYMBOL_1, SYMBOL_1, SYMBOL_2, EMPTY_SLOT], 
        [SYMBOL_2, SYMBOL_2, SYMBOL_1, EMPTY_SLOT],
        [EMPTY_SLOT, EMPTY_SLOT, SYMBOL_2, SYMBOL_1],
        [SYMBOL_1, SYMBOL_2],
        [EMPTY_SLOT, SYMBOL_2],
        [SYMBOL_1],
        [EMPTY_SLOT],
    ]
    assert expected == list(x.states for x in testee.state_as_diagonals())

  def test_add_counter_outside_range(self):
    testee = Grid()
    assert -1 == testee.add_counter(99, SYMBOL_1)

  def test_has_free_slots(self):
      testee = Grid(2, 2)
      testee.add_counter(0, SYMBOL_1)
      testee.add_counter(0, SYMBOL_1)
      testee.add_counter(1, SYMBOL_1)
      assert True == testee.has_free_slots()
      testee.add_counter(1, SYMBOL_1)
      assert False == testee.has_free_slots()