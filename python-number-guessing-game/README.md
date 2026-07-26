# Number Guessing Game

## Description
This is a simple Python number guessing game.

The program:
- Generates a random number.
- Takes input from the user.
- Handles invalid (non-integer) input using `try-except`.
- Continues until the correct number is guessed.
- Counts the number of attempts.
- Gives hints to guess a larger or smaller number.

## Features
- Random number generation
- Input validation
- Exception handling
- Unlimited attempts
- Guess counter

## Technologies Used
- Python 3
- random module

## How to Run

1. Clone the repository.
2. Open the project folder.
3. Run:

```bash
python main.py
```

## Example

```
Enter a number: 5
Enter larger

Enter a number: abc
Please enter a valid number.

Enter a number: 8
You guessed correctly in 3 attempts.
```