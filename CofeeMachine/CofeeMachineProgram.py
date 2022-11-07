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


def is_transaction_successful(money_received, cost_of_item):
    if money_received >= cost_of_item:
        change = round(money_received - cost_of_item,2)
        print(f"you have ${change} in change")
        global profit
        profit += cost_of_item
        return True
    else:
        print("sorry that is not enough money, money refunded")
        return False


def is_resource_enough(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there is not enough {item}")
            return False
    return True


def receive_money():
    print("please insert money")
    total = int(input("how many pesewas: ")) * 0.1
    total+= int(input("how many cedis: "))
    return total


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Your {drink_name} 🍵 is ready")


profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
machine_on = True

while machine_on:
    user_choice = input("What would you like? espresso/latte/cappuccino): \n")
    if user_choice.lower() == "off":
        machine_on = False
    elif user_choice.lower() == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Profit: ${profit}")
    else:
        user_order = MENU[user_choice]
        if is_resource_enough(user_order["ingredients"]):
            payment = receive_money()
            is_transaction_successful(payment, user_order["cost"])
            make_coffee(user_choice,user_order["ingredients"])










