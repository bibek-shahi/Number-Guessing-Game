# Number Guessing Game

A simple command-line Number Guessing Game built using Python.

The computer randomly selects a number between 1 and 100, and the player has to guess the correct number within a limited number of attempts. From https://roadmap.sh/projects/number-guessing-game

## Features

* Random number generation between 1 and 100
* Three difficulty levels:

  * Easy – 10 chances
  * Medium – 5 chances
  * Hard – 3 chances
* Higher or lower hints after each incorrect guess
* Tracks the number of attempts
* Displays a congratulatory message when the correct number is guessed

## How to Run

1. Make sure Python is installed on your computer.
2. Download or clone this repository.
3. Open a terminal or command prompt inside the project folder.
4. Run the program using:

```bash
python main.py
```

Replace `main.py` with your Python file name if your file has a different name.

## How to Play

1. Start the program.
2. Select a difficulty level.
3. Enter a number between 1 and 100.
4. The game will tell you whether the correct number is higher or lower than your guess.
5. Continue guessing until you find the correct number or use all your attempts.

## Example

```text
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter the difficulty level: 2

Great! You have selected the Medium difficulty level.
Let's start the game!

Guess the number: 50
Incorrect! The number is less than 50.

Guess the number: 30
Incorrect! The number is greater than 30.

Guess the number: 40
Congratulations! You guessed the correct number in 3 attempts.
```

## Future Improvements

Possible features that can be added later include:

* Play multiple rounds
* Timer
* Hint system
* High-score tracking
* Better input validation

## Technologies Used

* Python
* Python `random` module
* Command-line interface (CLI)

## Author

Created as a Python practice project to improve programming fundamentals such as conditions, loops, user input, and random number generation.
