import random

def choose_word():
    words = ["python", "programming", "challenge", "coding", "developer", "learning"]
    return random.choice(words)

def shuffle_word(word):
    shuffled_word = list(word)
    random.shuffle(shuffled_word)
    return ''.join(shuffled_word)

def play_spelling_game():
    print("Welcome to the Spelling Game!")
    original_word = choose_word()
    shuffled_word = shuffle_word(original_word)

    print("Here is a shuffled word:", shuffled_word) 

    attempts = 3
    while attempts > 0:
        guess = input("Your guess: ").lower()

        if guess == original_word:
            print("Congratulations! You guessed it correctly.")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect! You have {attempts} {'attempts' if attempts > 1 else 'attempt'} remaining.")
            else:
                print(f"Sorry, you're out of attempts. The correct word was '{original_word}'.")

if __name__ == "__main__":
    play_spelling_game()
