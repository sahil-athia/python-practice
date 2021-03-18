# a way to form new classes from predefined classes

# base class

class Animal():

  def __init__(self):
    print("ANIMAL CREATED")
  
  def who_am_i(self):
    print("I am an animal")
  
  def eat(self):
    print("I am eating")

my_animal = Animal()
my_animal.who_am_i()
my_animal.eat()

# dogs are animals
# dog is now a derrived class
class Dog(Animal):

  def __init__(self):
    # create instance of animal class when we create an instance of the dog class
    Animal.__init__(self)