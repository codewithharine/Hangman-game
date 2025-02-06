import random

def choose_word():
    words = ["python", "hangman", "developer", "programming", "artificial", "intelligence"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))
    
    while attempts > 0:
        guess = input("\nGuess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print(f"Good guess! {display_word(word, guessed_letters)}")
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
            guessed_letters.add(guess)

        if set(word) == guessed_letters:
            print("Congratulations! You've guessed the word:", word)
            break
    else:
        print("Game Over! The word was:", word)

if __name__ == "__main__":
    hangman()
