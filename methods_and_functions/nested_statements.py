# 
x = 50

def printer(x):
  print "X is {}".format(x)

  # LOCAL REASSIGNMENT
  x = 200
  print "reassigned x to {}".format(x)

def change_global():
  # if we wanted to change the golbal variable:
  global x
  print "X is {}".format(x)

  # REASSIGNMENT ON A GLOBAL LEVEL
  x = "new value"
  print "reassigned x to {}".format(x)

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

printer(x)
greet()
change_global()
print "x is: " + x