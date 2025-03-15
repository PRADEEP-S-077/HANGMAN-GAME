import random
import string

def choose_word():
    """Selects a random word from a predefined list."""
    words = ['python', 'developer', 'hangman', 'challenge', 'programming', 'professional']
    return random.choice(words).upper()

def display_word(word, guessed_letters):
    """Displays the word with guessed letters and underscores for remaining letters."""
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def get_valid_guess(guessed_letters):
    """Prompts the user for a valid letter input."""
    while True:
        guess = input("Enter a letter: ").upper()
        if len(guess) == 1 and guess in string.ascii_uppercase and guess not in guessed_letters:
            return guess
        print("Invalid input or letter already guessed. Try again.")

def hangman():
    """Main function to execute the Hangman game."""
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman! Try to guess the word.")
    
    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))
        print(f"Attempts left: {attempts}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        
        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess not in word:
            attempts -= 1
            print(f"Incorrect guess! You have {attempts} attempts left.")
        elif all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word: {word}")
            return
    
    print(f"Game Over! The word was: {word}")

if __name__ == "__main__":
    hangman()
