stock_prices = [("APPL", 255), ("GOOG", 500), ("MFST", 150)]

for tiker, price in stock_prices:
  # print tiker
  # print price
  pass

work_hours = [("Abby", 100), ("Billy", 400), ("Cassie", 250)]

def employee_check(work_hours):
  '''
    figure out who worked the most hours
  '''
  current_max = 0
  employee_of_month = ""

  for name, hours in work_hours:
    if hours > current_max:
      current_max = hours
      employee_of_month = name
    else:
      pass
  return(employee_of_month, current_max)

# we can unpack what the function returned us
name, hours = employee_check(work_hours)
print name
print hours