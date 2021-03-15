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

  # vars
  choice = "WRONG"
  acceptable_range = range(0, 10)
  within_range = False


  while choice.isdigit() == False or within_range == False:
    choice = "{}".format(input("Please Enter A Value (0-10): "))

    if choice.isdigit() == False:
      print("sorry that is not a digit")

    if choice.isdigit() == True:
      within_range = int(choice) in acceptable_range
        

  return int(choice)

user_choice()
# row1[user_choice()] = "X"
display(row1, row2, row3)
