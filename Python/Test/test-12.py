# Usage of decorators

def decor(func):
  def inner():
    func()
    print("How was your day? ")
  return inner
@decor
def greet():
  print("Good morning!")
greet()

# multiplication by third number
def decor(func):
  def inner():
    result= func()
    n3 = int(input("enter third number: "))
    result = result * n3
    return result
  return inner
@decor
def mult():
  n1 = int(input("enter first number: "))
  n2 = int(input("enter second number: "))
  prod = n1*n2
  return prod
print(mult())

# adding third number
def decor(func):
  def inner():
    result = func()
    n3 = float(input("enter third number: "))
    total = result + n3
    return total
  return inner
@decor
def add():
  n1 = float(input("enter first number: "))
  n2 = float(input("enter second number: "))
  result = n1+n2
  return result

print("addition is: ", add())