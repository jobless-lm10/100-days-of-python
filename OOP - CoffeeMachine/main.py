from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
coffee_machine = CoffeeMaker()
menu = Menu()
money = MoneyMachine()

def coffee_maker():
    global is_on
    user_input = input(f"What would you like? ({menu.get_items()}): ")
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        coffee_machine.report()
        money.report()
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        drink = menu.find_drink(user_input)
        if coffee_machine.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)

    if is_on:
        coffee_maker()


coffee_maker()