MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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


def resources_sufficient(order_ingredients):
    for ingredient in order_ingredients:
        if resources[ingredient] <= order_ingredients[ingredient]:
            print(f"Sorry not enough {ingredient}")
            return False
    return True


def process_coins():
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total


def make_coffee(drink, order_ingredients):
    for resource in resources:
        resources[resource] -= order_ingredients[resource]
    print(f"Here is your {drink} ☕")


profit = 0
is_on = True

while is_on:
    user_choice = input(print("What would you like? (espresso/latte/cappuccino): "))
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
        drink = MENU[user_choice]
        if resources_sufficient(drink["ingredients"]):
            money = process_coins()
            if money < drink["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                profit += round(money, 2)
                change = round(money - drink["cost"], 2)
                print(f"Here is ${change} in change")
                make_coffee(user_choice, drink["ingredients"])
