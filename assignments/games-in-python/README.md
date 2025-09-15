

# 📘 Assignment: Games in Python

## 🎯 Objective

Build a classic Hangman game in Python. You will practice string manipulation, loops, conditionals, and random selection by creating a word-guessing game where players try to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Hangman Game Implementation

#### Description
Create a Python program that lets a player guess letters to uncover a randomly selected word. The player has a limited number of incorrect guesses before the game ends.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Accept single-letter guesses from the user
- Display the current progress (e.g., _ _ a _ _ _)
- Track and display the number of incorrect guesses remaining
- End the game when the word is fully guessed or attempts are exhausted
- Show a win or lose message at the end

Example:
```text
Word: _ _ _ _ _
Guess a letter: a
Word: _ a _ _ _
Incorrect guesses left: 5
...etc...
```

### 🛠️ Optional: Add More Features

#### Description
Enhance your Hangman game with extra features to make it more fun or challenging.

#### Requirements
Completed program could:

- Allow the player to guess the whole word at once
- Show letters already guessed
- Add a visual representation (like ASCII art) for each incorrect guess
- Let the player play multiple rounds without restarting the program
