game_list = [0, 1, 2]

def display_game(game_list):
  print("here is the current list")
  print(game_list)

display_game(game_list)

def position_choice():
  choice = "WRONG"

  while choice not in ["0", "1", "2"]:
    choice = input("pick a position (0, 1, 2): ")

    if choice not in ["0", "1", "2"]:
      print("invalid choice")
    
  return int(choice)

position_choice()

def replacement_choice(game_list, position):
  user_placement = input("type a string to place at position {}: ".format(position))

  game_list[position] = user_placement

  return game_list


print(replacement_choice(game_list, 1))

def game_on_choice():
  choice = "WRONG"

  while choice not in ["Y", "N"]:
    choice = input("do you want to keep playing (Y or N)? ")

    if choice not in ["Y", "N"]:
      print("sorry i dont understand")
    
  if choice == "Y":
    return True
  else:
    return False


game_on_choice()

