# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
# TODO 3. Print report.
# TODO 4. Check resources sufficient?
# TODO 5. Process coins.
# TODO 6. Check transaction successful?
# TODO 7. Make Coffee.

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def process(coffee_option):
    global money_in_machine
    if resources['water'] < MENU[coffee_option]['ingredients']['water']:
        print("Sorry there is not enough water.")
    elif resources['milk'] < MENU[coffee_option]['ingredients']['milk']:
        print("Sorry there is not enough milk.")
    elif resources['coffee'] < MENU[coffee_option]['ingredients']['coffee']:
        print("Sorry there is not enough coffee.")
    else:
        cost = MENU[coffee_option]['cost']
        print("Please insert coins")
        quarter = int(input("how many quarters?: "))
        dime = int(input("how many dimes?: "))
        nickle = int(input("how many nickles?: "))
        pennie = int(input("how many pennies?: "))
        insert_coins = quarter * 0.25 + dime * 0.10 + nickle * 0.05 + pennie * 0.01
        if insert_coins > cost:
            money_in_machine += cost
            change = round(insert_coins - cost, 2)
            resources['water'] -= MENU[coffee_option]['ingredients']['water']
            resources['milk'] -= MENU[coffee_option]['ingredients']['milk']
            resources['coffee'] -= MENU[coffee_option]['ingredients']['coffee']
            print(f"Here is ${change} in change.")
            print("Here is your latte ☕️. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")


money_in_machine = 0
while True:
    option = input("What would you like? (espresso/latte/cappuccino): ")
    if option == "report":
        print(f"Water: {resources['water']}ml\n")
        print(f"Milk: {resources['milk']}ml\n")
        print(f"Coffee: {resources['coffee']}g\n")
        print(f"Money: ${money_in_machine}\n")
    elif option == "off":
        break
    else:
        process(option)
