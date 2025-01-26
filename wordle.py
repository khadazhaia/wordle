import random

# Introduce the game
print("Welcome to Wordle!\n")
print("You will get 6 chances to guess a 5-letter word!")
print("Each guess must be a 5-letter word.")
print("The word GREEN will populate if the letter is in the word and in the correct spot.")
print("The word YELLOW will populate if the letter is in the word but in the wrong spot.")
print("The word RED will populate if the letter isn't in the word.\n")

# Cet player name and pull a random word from the list 
def username(): 
    name = input("Please enter your name to start > ")
    return name
 
user_name = username()

word_list = ["slate", "brain", "cloud", "house", "dirty"] 

word = random.choice(word_list)

def player_guess(): 
  while True: 
    guess_word = input("Please enter a 5-letter word > ")
    
    if len(guess_word) > 5:
      print("Too many letters! Please enter a 5-letter word.\n")
    elif len(guess_word) < 5:
      print("Not enough letters! Please enter a 5-letter word.\n")
    else:
      break
    
  return guess_word

 # Tell the user if their guess had a correct letter in the right or wrong spot or not in the word
def check_guess(guess_word):
  number = 5
  while number > 0:
    if guess_word != word:
      print(f"You have {number} guesses left.\n")
      number -= 1
    else:
      print(f"Congratulations {user_name}! You guessed the word {word}!\n")
      return

    feedback = ["grey", "grey", "grey", "grey", "grey"]
    for i in range(len(guess_word)):
      if guess_word[i] == word[i]:
        feedback[i] = "green"
        print("GREEN\n")
      elif guess_word[i] in word:
        feedback[i] = "yellow"
        print("YELLOW\n")
      else:
        feedback[i] = "red"
        print("RED\n")

    guess_word = player_guess()

  print(f"You didn't guess the word {user_name}. It was {word}.\n")

# Ask the user if they want to play again and if not end the game
while True:
  guess_word = player_guess()
  check_guess(guess_word)
  play_again = input(f"Would you like to play again {user_name}? Type Y or N > ")
  if play_again.lower() != "y":
    print("Thank you for playing!")
    break

    