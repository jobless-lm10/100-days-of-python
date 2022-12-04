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
    "money": 0
}

is_on = True


# TODO: Check the user’s input to decide what to do next.
def ask_input():
    return input("What would you like? (espresso/latte/cappuccino) or 'report'/'off':").lower()


# TODO: Turn off the Coffee Machine by entering "off” to the prompt
def turn_off():
    global is_on
    is_on = False


# TODO: Print report
def report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {resources['money']}")


# TODO: Check resources sufficient?
def check_resources(drink):
    if MENU[drink]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
        return False
    if MENU[drink]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk.")
        return False
    if MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    return True


# TODO: Process coins.
def process_coins():
    quarters = int(input("How many 'Quarters'?: "))
    dimes = int(input("How many 'Dimes'?: "))
    nickles = int(input("How many 'Nickles'?: "))
    pennies = int(input("How many 'Pennies'?: "))
    return (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)


# TODO: Check transaction successful?
def transaction_check(amount, drink):
    if amount >= MENU[drink]["cost"]:
        resources["money"] += MENU[drink]["cost"]
        if amount > MENU[drink]["cost"]:
            print(f"Transaction successful. Here is your change ${amount - MENU[drink]['cost']:0.2f}.")
            return True
        print("Transaction successful")
        return True
    print("Sorry that's not enough money. Money refunded.")
    return False


# TODO: Make Coffee.
def make_coffee(drink):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    print(f"Here is your {drink}. Enjoy")


# Driver code
def coffee_maker():
    input = ask_input()
    if input == "off":
        turn_off()
    elif input == "report":
        report()
    elif input == "espresso" or input == "latte" or input == "cappuccino":
        if check_resources(input):
            amount = process_coins()
            if transaction_check(amount, input):
                make_coffee(input)

    if is_on:
        coffee_maker()


coffee_maker()
