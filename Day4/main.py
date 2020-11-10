import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

option = [rock,paper,scissors]

choose = input("What do you choose? Tpye 0 for rock, 1 for paper, 2 for scissors\n")

randon_choose = random.randint(0,2)

print(option[int(choose)])

print("Computer choose\n")

print(option[int(randon_choose)])

if(int(randon_choose) == int(choose)):
  print("Tie")
elif(int(randon_choose) == 0 and int(choose) == 2):
  print("You lose")
elif(int(randon_choose) == 1 and int(choose) == 0):
  print("You lose")
elif(int(randon_choose) == 2 and int(choose) == 1):
  print("You lose")
else:
  print("You win")