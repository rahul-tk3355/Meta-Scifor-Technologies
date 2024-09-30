#Q1.Random Password Generator
import random
import string

pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation
password = [random.choice(charValues) for _ in range(pass_len)]
print(''.join(password))

# #Q2. How do I make a GET  and post request using the requests module? and also checking status
# Random Quote Engine: Design a function that selects and displays a random quote from a predefined list.
#  https://api.quotable.io/random
#  https://api.chucknorris.io/jokes/random

import requests
def random_joke():
  url =  "https://api.chucknorris.io/jokes/random"
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    joke = data.get("value")
    print(f"joke: {joke}")
  else:
    print("permission denied!", response.status_code)
random_joke()

import requests
def random_quote():
  url =  " https://api.quotable.io/random"
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    quote = data.get("content")
    print(f"quote: {quote}")
  else:
    print("permission denied!", response.status_code)
random_quote()

