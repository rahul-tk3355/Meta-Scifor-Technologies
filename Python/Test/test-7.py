#Q1. Create a calculator using Classes and objects.

class Calculator:
  def __init__(self, a, b):
    self.a = a
    self.b = b
  def add(self):
    return self.a + self.b
  def sub(self):
    return self.a - self.b
  def mult(self):
    return self.a * self.b
  def div(self):
    return self.a / self.b
  def mod(self):
    return self.a % self.b
  def exp(self):
    return self.a ** self.b

calc1 = Calculator(10,5)
print(calc1.add())
print(calc1.sub())
print(calc1.mult())
print(calc1.div())
print(calc1.mod())
print(calc1.exp())

#Q2. Create a quiz using classes and objects.
class Quiz:
  def __init__(self):
    pass
  def quiz(self):
    q1 = input("Which is the largest animal in the world? ")
    if q1.lower() == 'blue whale':
      print("correct")
    else:
      print("wrong")
    q2 = int(input("What is the square root of 9? "))
    if q2 == 3:
      print("correct")
    else:
      print("wrong")
    q3 = input("Who is the founder of python language? ")
    if q3.lower() == 'guido van rossum':
      print("correct")
    else:
      print("wrong")
    q4 = input("Who is the CEO of OpenAI? ")
    if q4.lower() == 'sam altman':
      print("correct")
    else:
      print("wrong")
    q5 = input("Where is Thar desert? ")
    if q5.lower() == 'rajasthan':
      print("correct")
    else:
      print("wrong")
quiz1 = Quiz()
quiz1.quiz()