from random import *
def choose_word():
    word_list = ["globe", "spent", "chain", "pixel", "noble", "tiger", "orange", "space", "loyal", "peace", "ocean",
                 "donut",
                 "crane", "canoe", "lemon"]
    return choice(word_list)

def display_letters(available_letters):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]
    print("Available letters:", " ".join(letters))

def update_letters(available_letters, user_guess, correct_word):
    incorrect_letters = set(user_guess) - set(correct_word)
    for letter in incorrect_letters:
        if letter in available_letters:
            available_letters.remove(letter)


def display_wordle(user_guess, correct_word):
    BG_GREEN = "\u001b[42m"
    BG_YELLOW = "\u001b[43m"
    RESET = "\u001b[0m"

    for i in range(len(correct_word)):
        if user_guess[i] == correct_word[i]:
            print(BG_GREEN + user_guess[i] + RESET, end="")
        elif user_guess[i] in correct_word:
            print(BG_YELLOW + user_guess[i] + RESET, end="")
        else:
            print(user_guess[i], end="")
    print()


def play_wordle():
    print("WORDLE")
    correct_word = choose_word()
    available_letters = list("abcdefghijklmnopqrstuvwxyz")

    for n in range(6):
        display_letters(available_letters)
        user_guess = input("Guess the word: ").lower()

        update_letters(available_letters, user_guess, correct_word)
        display_wordle(user_guess, correct_word)

        if user_guess == correct_word:
            print("You win!")
            return

    print("You lose!")
    print("The correct word was", correct_word)

play_wordle()