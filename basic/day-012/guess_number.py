from random import randint

from arts import logo

def check_guess(guess: int) -> bool:
    """ Check if the guess is correct """
    if guess == number:
        print("You guessed the number!")
        return True
    
    if guess > number:
        print("Too high")
        return False
    
    if guess < number:
        print("Too low")
        return False

def get_attempts(mode_selected: str) -> int:
    """ Check the game mode entered by the user and return the number of attempts """
    try:
        attempts = GAME_MODES[mode_selected]
    except KeyError:
        print("Invalid game mode")
        exit()

    return attempts

GAME_MODES = {
    'easy': 10,
    'hard': 5,
}

number = randint(1, 100)

print(logo)
print("Welcome to the Guess Number Game! \nI am thinking of a number between 1 and 100.")
mode_selected = input("Type the game mode, if easy or hard: ").lower()
attempts = get_attempts(mode_selected)

while attempts > 0:
    print(f"You have {attempts} attempts left")
    guess = int(input("Guess the number: "))
    if check_guess(guess):
        exit()

    attempts -= 1

print(f"Too bad! The number was {number}")
