# 💣 Minesweeper — Python

A simple **terminal-based Minesweeper game** built using Python and NumPy.

The player has to uncover all safe cells without clicking on a mine. The game also supports flagging cells that the player thinks contain mines.

## 🎮 Features

* 🟩 10 × 10 game board
* 💣 Randomly generated mines
* 🎯 Three difficulty levels:

  * **Easy:** 15 mines
  * **Medium:** 20 mines
  * **Hard:** 25 mines
* 🚩 Flag and unflag cells
* 🔢 Displays the number of mines surrounding each revealed cell
* 🔄 Recursive cell revealing
* 🏆 Automatic win detection
* 💥 Mine detection and loss condition
* Uses NumPy to generate unique random mine positions

## 🛠️ Technologies Used

* **Python 3**
* **NumPy**

## 📦 Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd <your-repository-folder>
```

Install NumPy:

```bash
pip install numpy
```

## ▶️ How to Run

Run the Python file:

```bash
python main.py
```

You will be asked to select a difficulty:

```text
Enter your difficulty(Easy , Medium , Hard):
```

Enter:

```text
easy
```

or

```text
medium
```

or

```text
hard
```

## 🎮 How to Play

The board uses **row and column coordinates** from `0` to `9`.

For example:

```text
  0   1   2   3   4   5   6   7   8   9
0   |   |   |   |   |   |   |   |   |   |
1   |   |   |   |   |   |   |   |   |   |
2   |   |   |   |   |   |   |   |   |   |
...
```

When prompted:

```text
Enter your choice (row column 1 for flag / row column 0 for dig):
```

enter three values:

```text
row column action
```

### Dig a cell

Use `0` as the action.

Example:

```text
3 5 0
```

This digs the cell at:

```text
row = 3
column = 5
```

### Flag a cell

Use `1` as the action.

Example:

```text
3 5 1
```

This places a flag on the cell.

Entering the same command again removes the flag.

## 🔢 Numbers

A revealed number represents the number of mines in the surrounding cells.

For example:

```text
1 | 2 | 1
2 | X | 2
1 | 2 | 1
```

The `2` means that there are two mines among the surrounding cells.

The game checks all **8 possible neighboring cells**:

```text
↖  ↑  ↗
←  ■  →
↙  ↓  ↘
```

## 🏆 Winning

You win when all non-mine cells have been revealed.

The number of mines depends on the selected difficulty.

| Difficulty | Mines | Safe Cells |
| ---------- | ----: | ---------: |
| Easy       |    15 |         85 |
| Medium     |    20 |         80 |
| Hard       |    25 |         75 |

## 💥 Losing

If you dig a cell containing a mine:

```text
You lost
```

and the game ends.

## 🧠 Concepts Used

This project was built to practice several Python programming concepts:

* Functions
* Global variables
* Lists
* Loops
* Conditional statements
* Recursion
* NumPy arrays
* Random number generation
* Array indexing
* Coordinate calculations
* Input handling
* Basic game-state management

## 📁 Project Structure

```text
Minesweeper/
│
├── main.py
└── README.md
```

## 🔮 Future Improvements

Possible improvements for future versions:

* [ ] Implement standard Minesweeper zero-cell expansion
* [ ] Add input validation
* [ ] Prevent digging flagged cells
* [ ] Add a restart option
* [ ] Add a timer
* [ ] Add a score system
* [ ] Add customizable board sizes
* [ ] Add more difficulty levels
* [ ] Improve the terminal UI
* [ ] Add a graphical interface using Tkinter or Pygame
* [ ] Refactor the project using classes and object-oriented programming

## 📜 License

This project is open-source and available for learning and personal use.
