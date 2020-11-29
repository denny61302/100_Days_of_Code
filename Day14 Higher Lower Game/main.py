# Generate a random account from the game data.
# Format account data into printable format.
# Ask user for a guess.
# Check if user is correct.
  ## Get follower count.
  ## If Statement
# Feedback.
# Score Keeping.
# Make game repeatable.
# Make B become the next A.
# Add art.
# Clear screen between rounds.

import random
import art
import game_data
from replit import clear

def compare_win(data_a, data_b, choice):
  high = 0
  if data_a['follower_count'] > data_b['follower_count']:
    high = data_a['follower_count']
  else:
    high = data_b['follower_count']

  if choice == "A":
    if data_a['follower_count'] == high:
      return False
    else:
      return True
  elif choice == "B":
    if data_b['follower_count'] == high:
      return False
    else:
      return True

you_loss = False
score = 0

data_b = random.choice(game_data.data)

while not you_loss:
  print(art.logo)
  
  data_a = data_b
  data_b = random.choice(game_data.data)

  while data_a == data_b:
    data_b = random.choice(game_data.data)

  if score > 0:
    print(f"You're right! Current score: {score}.")
  
  print(f"Compare A: {data_a['name']}, a {data_a['description']}, from {data_a['country']}")
  print(art.vs)
  print(f"Aganist B: {data_b['name']}, a {data_b['description']}, from {data_b['country']}")

  choice = input("Who has more followers? Type 'A' or 'B': ")

  you_loss = compare_win(data_a, data_b, choice)
  if not you_loss:
    score += 1
  
  clear()
  
if you_loss:
  clear()
  print(art.logo)
  print(f"Sorry, that's wrong. Final score: {score}")