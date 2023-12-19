import random

def choose_word():
    words = ["python", "hangman", "programming", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def display_hangman(attempts):
    stages = [  # Final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # Head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # Head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # Head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # Head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # Head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # Initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[attempts]

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6  # Number of allowed wrong guesses

    print("Welcome to Hangman!")

    while attempts > 0:
        print(display_hangman(attempts))
        print("\nGuessed letters:", " ".join(sorted(guessed_letters)))
        print("\nWord:", display_word(word, guessed_letters))
        
        guess = input("\nGuess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
        
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You've guessed the word:", word)
            return

    print(display_hangman(attempts))
    print("\nSorry, you've run out of guesses. The word was:", word)

hangman()
