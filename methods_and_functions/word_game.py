
def first_user_choice():
  choice = "WRONG"

  while choice.isdigit() == False:
    choice = "{}".format(input("you are stuck in a house, which door would you like to take? 1 or 2: "))

  return int(choice)

def second_user_choice():
  choice2 = "WRONG"

  while choice2.isdigit() == False:
    choice2 = "{}".format(input("you are inside of the basement, do you enter 1: celler or 2: sneak out window: "))
  
  return int(choice2)

def third_user_choice():
  choice3 = "WRONG"

  while choice3.isdigit() == False:
    choice3 = "{}".format(input("you managed to escape into the backyard, do 1: run to the road or 2: call for help "))
  
  return int(choice3)

answer1 = first_user_choice()

if answer1 == 1:
  print("wrong door you died")


answer2 = second_user_choice()

if answer2 == 2:
  print("a killer waited for you outside, you died")

answer3 = third_user_choice()

if answer3 == 2:
  print("a killer managed to get you during the call, you died")


