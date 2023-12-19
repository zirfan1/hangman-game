import getpass

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def display_hangman(wrong_guesses):
    stages = [
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """
    ]
    return stages[wrong_guesses]

def hangman():
    print("Player 1: Enter a word for Player 2 to guess.")
    word = getpass.getpass("Enter word: ").lower()

    guessed_letters = set()
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("\n" * 50)
    print("Welcome to Hangman! Player 2, start guessing.")

    while wrong_guesses < max_wrong_guesses:
        print(display_hangman(wrong_guesses))
        print("\nGuessed letters:", " ".join(sorted(guessed_letters)))
        print("\nWord:", display_word(word, guessed_letters))
        
        guess = input("\nGuess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            wrong_guesses += 1
            print(f"Wrong guess! You have {max_wrong_guesses - wrong_guesses} attempts left.")
        else:
            print("Good guess!")

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations, Player 2! You've guessed the word:", word)
            return

    print(display_hangman(wrong_guesses))
    print("\nSorry, Player 2. You've run out of guesses. The word was:", word)

def display_menu():
    print("1. Play Game")
    print("2. Exit Game")
    print("3. Restart Game")
    return input("Enter your choice (1-3): ")

def main():
    while True:
        choice = display_menu()

        if choice == "1":
            hangman()
        elif choice == "2":
            print("Exiting game. Goodbye!")
            break
        elif choice == "3":
            print("Restarting game...")
            continue
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

