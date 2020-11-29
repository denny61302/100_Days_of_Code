import random
import art

print(art.logo)
random_num = random.randint(1,100)
# print(random_num)
correct = False
level = input("Choose a level, 'h' for high, 'l' for low: ")
if level == "h":
  life = 5
elif level == "l":
  life = 10 

while not correct and life > 0:
  number = int(input("Guess a number: "))
  if random_num > number:
    print("Higher\n")
    life -= 1
    print(f"You still have {life} life to guess\n")  
  elif random_num < number:
    print("Lower\n")
    life -= 1
    print(f"You still have {life} life to guess\n")  
  elif random_num == number:
    print("Correct\n")  
    correct = True

if not correct:
  print("Lose")


