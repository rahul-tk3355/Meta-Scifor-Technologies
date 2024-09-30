
# Q1
def add_numbers(a, b):
  return a + b


def sub_numbers(a, b):
  return a - b


def mul_numbers(a, b):
  return a * b


print(add_numbers(2, 3))
print(sub_numbers(5, 3))
print(mul_numbers(6, 7))

#Q2


def simple_interest(p, t, r):
  return (p * t * r) / 100


def com_interest(p, t, r):
  return p * (1 + r / 100)**t


print(simple_interest(100, 2, 10))
print(com_interest(1000, 2, 5))

#Q3
def is_perfect_square(num):
  if num < 0:
    return False
  if num == 0 or num == 1:
    return True
  for i in range(num):
    if i * i == num:
      return True

num = int(input("enter the number: "))
print(is_perfect_square(num))

#Q4
def toWord(num):
  digit_to_word = {
    '0' : 'zero',
    '1' : 'one',
    '2' : 'two',
    '3' : 'three',
    '4' : 'four',
    '5' : 'five',
    '6' : 'six',
    '7' : 'seven',
    '8' : 'eight',
    '9' : 'nine'
  }
  num_str = str(num)
  word = []

  for digit in num_str:
    if digit in digit_to_word:
      word.append(digit_to_word[digit])
  return ('-'.join(word))
num = int(input("enter the number: "))
print(toWord(num))

#Q5
def fashion_factory(total_stock, sold_stocks):
  available_stock = total_stock - sold_stocks
  available_stock_in_percent = (available_stock/total_stock)*100
  print(f'Avialable stock: {available_stock_in_percent:.2f}%')

def rosebud(total_stock, sold_stocks):
  available_stock = total_stock - sold_stocks
  available_stock_in_percent = (available_stock/total_stock)*100
  print(f'Avialable stock: {available_stock_in_percent:.2f}%')

def Oak_and_Pine(total_stock, sold_stocks):
  available_stock = total_stock - sold_stocks
  available_stock_in_percent = (available_stock/total_stock)*100
  print(f'Avialable stock: {available_stock_in_percent:.2f}%')

def Loire_Valley(total_stock, sold_stocks):
  available_stock = total_stock - sold_stocks
  available_stock_in_percent = (available_stock/total_stock)*100
  print(f'Avialable stock: {available_stock_in_percent:.2f}%')

fashion_factory(100,30)
rosebud(120,50)
Oak_and_Pine(90,20)
Loire_Valley(110,45)
