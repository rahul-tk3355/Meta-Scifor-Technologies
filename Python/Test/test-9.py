
# creating a calculator using single inheritance
class Calculator:
  def __init__(self, a, b):
    self.a = a
    self.b = b
class Calc_operations(Calculator):
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
calc1 = Calc_operations(10,5)
print(calc1.add())
print(calc1.sub())
print(calc1.mult())
print(calc1.div())
print(calc1.mod())
print(calc1.exp())

# sum of 100 numbers using single inheritance
class Sum:
  def __init__(self):
    pass
class Add(Sum):
  def sum(self):
    sum = 0
    for val in range(100):
      sum+=val
    return sum
s1 = Add()
print(s1.sum())