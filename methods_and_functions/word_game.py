
def user_choice():
  choice = "WRONG"

  while choice.isdigit() == False:
    choice = "{}".format(input("you are stuck in a house, which door would you like to take? 1 or 2: "))

  return int(choice)

answer1 = user_choice()

if answer1 == 1:
  print("you chosse answer 1")
elif answer1 == 2:
  print("you chosse answer 2")