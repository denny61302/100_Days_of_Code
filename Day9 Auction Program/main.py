from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)

keep_going = True
data = []
while keep_going:
  new_data = {}
  name = input("What is your name? \n")
  bid = int(input("How much is your bid? \n"))
  new_data["name"] = name
  new_data["bid"] = bid
  data.append(new_data)
  option = input("Do you want to continue? Yes or No \n").lower()

  if option == "no":
    keep_going = False
  else:
    clear()

winner = ""
winner_bid = 0
for single_entry in data:
  if single_entry["bid"] > winner_bid:
    winner_bid = single_entry["bid"]
    winner =single_entry["name"]

print(f"Winner is {winner}, the final bid is {winner_bid}")
 