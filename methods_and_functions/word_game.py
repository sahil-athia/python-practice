
def first_user_choice():
  choice = "WRONG"

  while choice.isdigit() == False:
    choice = "{}".format(input("you are stuck in a house, which door would you like to take? 1 or 2: "))

  return int(choice)

def second_user_choice():
  choice = "WRONG"

  while choice.isdigit() == False:
    choise = "{}".format(input("you are inside of the basement, do you enter 1: celler or 2: sneak out window: "))
  
  return int(choice)

answer1 = first_user_choice()

if answer1 == 1:
  print("wrong door you died")


answer2 = second_user_choice()

if answer2 == 2:
  print("a killer waited for you outside, you died")