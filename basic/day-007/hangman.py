# ASCII vy:
# https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c

import random

HANGMAN_TITLE = """

  o         o                                                                               
 <|>       <|>                                                                              
 < >       < >                                                                              
  |         |      o__ __o/  \o__ __o     o__ __o/  \o__ __o__ __o      o__ __o/  \o__ __o  
  o__/_ _\__o     /v     |    |     |>   /v     |    |     |     |>    /v     |    |     |> 
  |         |    />     / \  / \   / \  />     / \  / \   / \   / \   />     / \  / \   / \ 
 <o>       <o>   \      \o/  \o/   \o/  \      \o/  \o/   \o/   \o/   \      \o/  \o/   \o/ 
  |         |     o      |    |     |    o      |    |     |     |     o      |    |     |  
 / \       / \    <\__  / \  / \   / \   <\__  < >  / \   / \   / \    <\__  / \  / \   / \ 
                                                |                                           
                                        o__     o                                           
                                        <\__ __/>                                           

"""
HANGMANPICS = ["""
  +---+
  |   |
      |
      |
      |
      |
=========""", """
  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]

fruits = [
  "apple", 
  "banana", 
  "cherry", 
  "date", 
  "elderberry", 
  "fig", 
  "grape", 
  "honeydew", 
  "kiwi", 
  "lemon", 
  "mango", 
  "nectarine", 
  "orange", 
  "peach", 
  "pear", 
  "quince", 
  "raspberry", 
  "strawberry", 
  "tangerine", 
  "ugli fruit", 
  "watermelon"]

word = random.choice(fruits)
word_list = []
word_list[:0] = word

errors = 0

print(HANGMAN_TITLE)
guessing = ["_" for i in range(len(word))]
end_of_game = False

while end_of_game == False:
    print(f"The word to guess: {' '.join(guessing)}\n")
    guess = input("Guess a letter: ").lower()
    if guess in word:
        print("You guessed a letter!")
        guess_list = [index for index in range(len(word)) if guess == word[index]]
        for i in guess_list:
            guessing[i] = guess

        if '_' not in guessing:
            print("You won!")
            print(f"The word is: {''.join(guessing)}\n")
            end_of_game = True
    else:
      print(HANGMANPICS[errors])
      print(f"You have {len(HANGMANPICS) - errors - 1} guesses left!")
      errors += 1
      if errors == len(HANGMANPICS):
        print("You lost!")
        print(f"The word is: {''.join(word)}\n")
        end_of_game = True
