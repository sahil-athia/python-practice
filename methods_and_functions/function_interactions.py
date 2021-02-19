# lets mimic three cup monte with functions

from random import shuffle

def shuffle_list(my_list):
  '''
  used to shuffle the list containing the 'ball'
  '''
  shuffle(my_list)
  return my_list

def player_guess():
  '''
  we need to grab the users guess, we will loop while their guess is not 0, 1 or 2
  '''
  guess = ''

  while guess not in [0, 1, 2]:
    guess = input("pick a number: 0, 1 or 2: ")
  
  return int(guess)

def check_guess(my_list, guess):
  if my_list[guess] == "O":
    print("Correct")
  else:
    print("Wrong Guess")
    print my_list



# INITIAL LIST
example = [' ', ' ', 'O']

# MIX LIST
mixed_list = shuffle_list(example)

# USER GUESS
my_index = player_guess()

# CHECK GUESS
check_guess(mixed_list, my_index)
