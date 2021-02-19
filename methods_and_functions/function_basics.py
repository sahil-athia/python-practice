# def keyword is used to define function
# this is followed my the function name (generally snake_cased)
# def function_name():
#   ''' optional doc string to describe function ''' (triple quoted)
#   print("hello")
# to execute call function with parenthesis

def say_hello(name = "default"):
  '''
    This function will say hello to a person
    provides default if no arguments are given
  '''
  print("Hello " + name )

def get_sum(a, b):
  return a + b

say_hello("bob")
say_hello()
result = get_sum(3, 7)
print(result)
