def display(row1, row2, row3):
  print(row1)
  print(row2)
  print(row3)

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
display(row1, row2, row3)
row2[1] = "X"
display(row1, row2, row3)

def user_choice():
  choice = "WRONG"

  while choice.isdigit() == False:
    choice = "{}".format(input("Please Enter A Value (0-10): "))

    if choice.isdigit() == False:
      print("sorry that is not a digit")

  return int(choice)

user_choice()
# row1[user_choice()] = "X"
display(row1, row2, row3)
