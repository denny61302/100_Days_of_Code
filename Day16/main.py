from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def process(coffee_option):
    drink = menu.find_drink(coffee_option)
    if coffee_maker.is_resource_sufficient(drink):
        if money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


while True:
    option = input("What would you like? (espresso/latte/cappuccino): ")
    if option == "report":
        coffee_maker.report()
        money_machine.report()
    elif option == "off":
        break
    else:
        process(option)
