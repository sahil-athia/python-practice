# 
x = 50

def printer(x):
  print "X is {}".format(x)

  # LOCAL REASSIGNMENT
  x = 200
  print "reassigned x to {}".format(x)

printer(x)


# num in the following is a local variable
lambda num : num * 2

# GLOBAL
name = "this is a global string"

def greet():
  # ENCLOSING
  name = "sammy"

  def hello():
    # LOCAL
    name = "local"

    print "hello " + name
  hello()

greet()