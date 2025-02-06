# Hangman-game
A classic Hangman game where you guess letters to reveal a word, with limited wrong attempts
# Hangman Game

## Overview
This is a classic Hangman game where you need to guess the word by suggesting letters. The game will display the correctly guessed letters and blanks for the remaining ones. You have a limited number of attempts to guess the word correctly.

## Features
- Randomly selects a word from a predefined list.
- Displays the word with blanks for unguessed letters.
- Allows you to guess one letter at a time.
- Gives feedback on correct and incorrect guesses.
- Limits the number of wrong attempts to 6.
- Ends when the word is guessed or the attempts run out.

## How to Play
1. Start the game by running the program.
2. You will be prompted to guess a letter.
3. The game will show the word with blanks for unguessed letters.
4. Continue guessing until:
   - You guess all the letters correctly, or
   - You run out of attempts (6 wrong guesses).
5. The game will notify you if you've won or lost.

## Requirements
- Python 3.x

## Installation
1. Clone the repository or download the source code.
   ```bash
   git clone https://github.com/your-username/hangman-game.git

   
Code Explanation
Functions:
choose_word: Randomly selects a word from a predefined list of words.
display_word: Displays the word with guessed letters and underscores for unguessed letters.
hangman: Main function that runs the game, handles user input, and controls the flow of the game.

Example
Welcome to Hangman!
_ _ _ _ _ _ _ _

Guess a letter: p
Good guess! p _ _ _ _ _ _ _

Guess a letter: o
Good guess! p _ _ o _ _ _

Guess a letter: z
Wrong guess! You have 5 attempts left.

...
