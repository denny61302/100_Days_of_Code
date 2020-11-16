
import random
import art
from replit import clear

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "It's a draw"
  elif computer_score == 0:
    return "Computer go the blackjack! You lose"
  elif user_score == 0:
    return "You got the blackjack! You win"
  elif user_score > 21:
    return "Computer wins"
  elif computer_score > 21:
    return "You win"
  elif user_score > computer_score:
    return "You win"
  else:
    return "Computer wins"  

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
  if len(cards) == 2 and sum(cards) == 21:      
    return 0 

  if sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)

  return sum(cards)
  
def game():
  print(art.logo)
  user_cards = []
  computer_cards = []

  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  end_game = False
  while not end_game:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your card {user_cards}, score {user_score}")
    print(f"Computer card {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      end_game = True
    else:
      option = input("want to draw another card, yes or no? ")
      if option == "yes":
        user_cards.append(deal_card())
      else:
        end_game = True

  while computer_score < 17 and computer_score != 0:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
    
  print(f"Your final hand {user_cards}, final score {user_score}")
  print(f"Computer's final hand {computer_cards}, final score {computer_score}")

  print(compare(user_score, computer_score))

while input("Start a game, yes or no? ") == "yes":  
  clear()
  game()
  