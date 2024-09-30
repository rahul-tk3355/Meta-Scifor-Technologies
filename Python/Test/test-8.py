
class Triangle:
  def __init__(self):
    pass
  def perimter(self,side):
    return 3*side
  def rect_area(self, length, breadth):
    return length*breadth
  def sq_area(self, side):
    return (4*side)
  def circle_area(self, radius):
    return 3.14*radius**2

t1 = Triangle()
print(t1.perimter(4))
print(t1.rect_area(4,3))
print(t1.sq_area(5))
print(t1.circle_area(4))

# factorial
class Factorial:
  def __init__(self):
    pass
  def fact(self, n):
    return n*fact(n-1)
fc = Factorial()
print(fc.fact(5))

# sum of 1000 numbers
class Sum:
  def __init__(self):
    pass

  def sum(self):
    sum = 0
    for val in range(1000):
      sum+=val
    return sum
s1 = Sum()
print(s1.sum())

# fibonacci series
class Fibonacci:
  def __init__(self):
    pass
  def fib_series(self, n):
    a = 0
    b = 1
    if n==1:
      print(a)
    else:
      print(a)
      print(b)
    for i in range(2,n):
      c = a+b
      a = b
      b = c
      print(c)
f1 = Fibonacci()
f1.fib_series(10)