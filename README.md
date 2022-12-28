Connect 4
=====

Connect 4 is a strategy game where players take turns to drop counters into a grid.
The first player to line up 4 counters in a row, either horizonally, vertically or diagonally is the winner.

You can read more [here](https://en.wikipedia.org/wiki/Connect_Four)

### Setting up

The game is written in the [Python](https://www.python.org/) programming language and uses the [Poetry](https://python-poetry.org/) framework to simplify project and package management.

When you have a working Python3 environment, Poetry can be installed with this command (on Linux, Mac or Windows).

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Further setup docs are [here](https://python-poetry.org/docs/)

The project dependencies (only Pytest) are installed by running the following in the project root.

```bash
poetry install
```

### Running the tests

The tests can be run via:

```bash
poetry run pytest
```

### Running the game

The game can be started via:

```bash
poetry run python c4/game.py
```

It asks each user in turn for their name then displays the grid

```bash
poetry run python c4/game.py
What is your name player 1? Player 1
What is your name player 2? Player 2

|.|.|.|.|.|.|.|
|.|.|.|.|.|.|.|
|.|.|.|.|.|.|.|
|.|.|.|.|.|.|.|
|.|.|.|.|.|.|.|
|.|.|.|.|.|.|.|

Where would you like to drop your token Player 1 [0-6]? 0
```

By default the grid is 6x7 in size and each player in turn must drop their counter in a column (0 is furthest left, 6 furthest right)

Eventually a winner emerges!

```bash
Where would you like to drop your token Player 1 [0-6]? 3

|.|.|.|.|.|.|.|
|.|.|.|.|.|.|.|
|.|.|.|.|.|.|.|
|.|.|.|.|.|.|.|
|.|.|.|.|.|.|.|
|x|x|x|x|o|o|o|


Congratulations Player 1 you have won the game!!!
```

Have fun!!