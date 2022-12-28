from collections import defaultdict
from collections.abc import Iterable, Generator
from itertools import groupby

EMPTY_SLOT = '.'

class GridState:
  '''Represents a row, column or diagonal in the game'''
  def __init__(self):
    self.states = []

  def add_state(self, state: str):
    '''Add a new grid state'''
    self.states.append(state)

  def add_states(self, states:Iterable[str]):
    '''Add multiple grid states'''
    self.states.extend(states)

  def is_winner(self) -> bool:
    '''Group the consecutive states, filter empty and see if any have 4 or more matches'''
    groups = groupby(self.states)
    consec_groups = [(token, sum(1 for _ in group)) for token, group in groups]
    for _, count in filter(lambda consec_tup: consec_tup[0] != EMPTY_SLOT, consec_groups):
      if count >= 4:
        return True
    return False

  def __str__(self) -> str:
    return str(self.states)

class Column:
  '''Represents a column of tokens or spaces in the grid'''
  def __init__(self, height: int):
    self.slots = []
    for _ in range(height):
      self.slots.append(EMPTY_SLOT)

  def last_empty_slot(self) -> int:
    '''Finds the index of the LAST empty slot in the column (closest to bottom)'''
    try:
      return len(self.slots)-self.slots[::-1].index(EMPTY_SLOT)-1
    except ValueError:
      return -1

  def add(self, token: str) -> int:
    '''Add a token to the column, works from bottom up (uses last available slot)'''
    last_empty_slot = self.last_empty_slot()
    if last_empty_slot > -1:
      self.slots[last_empty_slot] = token
    return last_empty_slot

  def height(self) -> int:
    '''Represents the height of the column'''
    return len(self.slots)

  def show(self, level: int) -> None:
    '''Display the current column state at this level'''
    print('{}|'.format(self.slots[level]), end='')

class Grid:
  '''Represents a game grid'''
  def __init__(self, width: int=7, height: int=6):
    self.columns = []
    self.width = width
    for _ in range(width):
      self.columns.append(Column(height))

  def add_counter(self, column_idx: int, token: str) -> int:
    '''Adds a counter to the grid at column specified'''
    if column_idx > self.column_count():
      return -1
    return self.columns[column_idx].add(token)

  def row_count(self) -> int:
    '''Return the number of rows in the grid'''
    if len(self.columns) == 0:
      return 0
    return self.columns[0].height()

  def column_count(self) -> int:
    '''Return the number of columns in the grid'''
    return len(self.columns)

  def state_as_columns(self) -> Generator[GridState, None, None]:
    '''Return the grid columns as GridState objects'''
    for column in self.columns:
      grid_state = GridState()
      grid_state.add_states(column.slots)
      yield grid_state

  def state_as_rows(self) -> Generator[GridState, None, None]:
    '''Return the grid rows as GridState objects'''
    for idx in range(self.row_count()):
      row_grid_state = GridState()
      for column in self.columns:
        row_grid_state.add_state(column.slots[idx])
      yield row_grid_state

  def state_as_diagonals(self) -> Generator[GridState, None, None]:
    '''Return the diagonals (both directions) as GridState objects'''
    d = defaultdict(list)
    for rc in range(self.row_count()):
      for cc in range(self.column_count()):
        target = self.columns[cc].slots[rc]
        d[cc-rc].append(target)
        d[cc+rc].append(target)
    for diag in d.values():
      grid_state = GridState()
      grid_state.add_states(diag)
      yield grid_state

  def show(self) -> None:
    '''Display the current grid state'''
    for idx in range(self.row_count()):
      print('|', end='')
      for column in self.columns:
        column.show(idx)
      print('')
