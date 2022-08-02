def product(num, *args):
  for arg in args:
    num *= arg
  print(num)

product(-1, 4) # returns -4
product(2, 5, 5) # returns 50
product(4, 0.5, 5) # returns 10.0