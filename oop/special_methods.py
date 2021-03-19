my_list = [1, 2, 3]
print(len(my_list))

class Book():

  def __init__(self, title, author, pages):
    self.title = title
    self.author = author
    self.pages = pages 
  
  def __str__(self):
    return f"{self.title} by {self.author}"
  
  def __len__(self):
    return self.pages

b = Book("title", "person", 90)
print(b)
print(len(b))

# we can delete b using del b, and print a report when it happens
