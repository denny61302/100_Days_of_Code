#Calculator

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def sub(n1, n2):
  return n1 - n2

#Multiply
def mul(n1, n2):
  return n1 * n2

#Divide
def div(n1, n2):
  return n1 / n2

ops = {
  "+":add, 
  "-":sub, 
  "*":mul, 
  "/":div
}

def calculate():
  keep_going = True

  num1 = int(input("What's is the first number? "))

  while keep_going:

    
    operand = input("What do you want to calculate? ")
    num2 = int(input("What's is the next number? "))

    function = ops[operand]

    ans = function(num1,num2)
    print(f" {num1} {operand} {num2} = {ans}")

    option = input("Do you want to continue? Yes or No ").lower()

    if option == "yes":
      num1 = ans
    else:
      keep_going = False
      calculate()

calculate()


