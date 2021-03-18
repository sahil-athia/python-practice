class Dog():
  
  def __init__(self, breed, name, spots):
    self.breed = breed
    self.name = name

    # expected boolean
    self.spots = spots


my_dog = Dog(breed = "lab", name="dawg", spots=False)
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)