from grid import Grid

PLAYER_1_TOKEN = 'x'
PLAYER_2_TOKEN = 'o'

GAME_STATE_IN_PROGRESS = 0
GAME_STATE_WINNER = 1
GAME_STATE_BAD_INPUT = 2
GAME_STATE_DRAW = 3

class Player:
  '''Represents a player of the game'''

  def __init__(self, name, token):
    self.name = name
    self.token = token

class ConnectFourGame:
  '''Represents a game session of the Connect 4 game'''
  def __init__(self, player1: str, player2: str, grid_width: int=7, grid_height: int=6):
    self.game_grid = Grid(grid_width, grid_height)
    self.current_player = Player(player1, PLAYER_1_TOKEN) # Player1 is first by default
    self.previous_player = Player(player2, PLAYER_2_TOKEN)

  def show_grid(self) -> None:
    '''Print the current state of the game'''
    print()
    self.game_grid.show()
    print()

  def check_state(self) -> int:
    '''Check the game state for a winner, or else continue'''
    for c in self.game_grid.state_as_columns():
      if c.is_winner():
        return GAME_STATE_WINNER
    for r in self.game_grid.state_as_rows():
      if r.is_winner():
        return GAME_STATE_WINNER
    for d in self.game_grid.state_as_diagonals():
      if d.is_winner():
        return GAME_STATE_WINNER
    return GAME_STATE_IN_PROGRESS

  def switch_player(self) -> None:
    '''Switch the current player'''
    previous_player = self.previous_player
    self.previous_player = self.current_player
    self.current_player = previous_player

  def update_grid(self, column: int, player_token: str) -> int:
    '''Update the game grid'''
    return self.game_grid.add_counter(int(column), player_token)

  def take_turn(self) -> int:
    '''Take a turn at the game'''
    column = input(
      'Where would you like to drop your token {} [0-{}]? '.format(
        self.current_player.name, self.game_grid.column_count()
      ))
    result = self.update_grid(int(column), self.current_player.token)
    if result < 0:
      return GAME_STATE_BAD_INPUT
    if self.game_grid.has_free_slots() is False:
      return GAME_STATE_DRAW
    return self.check_state()

def start_game() -> None:
  first_player = input('What is your name player 1? ')
  second_player = input('What is your name player 2? ')
  game = ConnectFourGame(first_player, second_player)
  game.show_grid()
  while True:
    current_state = game.take_turn()
    game.show_grid()
    if current_state == GAME_STATE_WINNER or current_state == GAME_STATE_DRAW:
      break
    if current_state == GAME_STATE_BAD_INPUT:
      print('Oops! The column you specified is either full or out of range, please try again! ')
      print()
      continue
    game.switch_player()
  print()
  if current_state == GAME_STATE_WINNER:
    print('Congratulations {} you have won the game!!!'.format(game.current_player.name))
  else:
    print('There are no spaces left in the grid!! The game is a draw.')
  print()

def main() -> None:
  start_game()

if __name__ == '__main__':
  main()