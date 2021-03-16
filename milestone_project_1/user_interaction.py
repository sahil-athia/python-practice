game_list = [0, 1, 2]
game_on = True

def display_game(game_list):
  print("here is the current list")
  print(game_list)


def position_choice():
  '''
  let the user choose the position on the game list to be changed 
  '''
  choice = "WRONG"

  while choice not in ["0", "1", "2"]:
    choice = input("pick a position (0, 1, 2): ")

    if choice not in ["0", "1", "2"]:
      print("invalid choice")
    
  return int(choice)


def replacement_choice(game_list, position):
  '''
  user can decide what to change the position chosen earlier with
  '''
  user_placement = input("type a string to place at position {}: ".format(position))

  game_list[position] = user_placement

  return game_list


def game_on_choice():
  '''
  allows user to leave or keep playing
  '''
  choice = "WRONG"

  while choice not in ["Y", "N"]:
    choice = input("do you want to keep playing (Y or N)? ")

    if choice not in ["Y", "N"]:
      print("sorry i dont understand")
    
  if choice == "Y":
    return True
  else:
    return False

while game_on:
  display_game(game_list)

  position = position_choice()

  game_list = replacement_choice(game_list, position)

  display_game(game_list)

  game_on = game_on_choice()