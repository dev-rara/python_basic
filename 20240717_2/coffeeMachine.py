MENU = {    "espresso": {        "ingredients": {            "water": 50,            "coffee": 18,        },        "cost": 1.5,    },    "latte": {        "ingredients": {            "water": 200,            "milk": 150,            "coffee": 24,        },        "cost": 2.5,    },    "cappuccino": {        "ingredients": {            "water": 250,            "milk": 100,            "coffee": 24,        },        "cost": 3.0,    }}profit = 0resources = {    "water": 300,    "milk": 200,    "coffee": 100,}# 주문한 메뉴 재료 확인def checkResourceSufficient(order_ingredients):    for item in order_ingredients:        if order_ingredients[item] > resources[item]:            print(f'Sorry there is not enough {item}')            return False    return True# 투입된 동전 종류별 더하기 [quarters(0.25), dimes(0.1), nickles(0.05), pennies(0.01)]def processCoins():    print('Please insert coins.')    total = int(input('how many quarters?: ')) * 0.25    total += int(input('how many dimes?: ')) * 0.1    total += int(input('how many nickles?: ')) * 0.05    total += int(input('how many pennies?: ')) * 0.01    return total# 받은 돈 더하고, 남는 돈 돌려 주기def isTransactionSuccessful(received_coins, drink_cost):    if received_coins >= drink_cost:        change = round(received_coins - drink_cost, 2)        print(f'Here is {change} in change.')        global profit        profit += drink_cost        return True    else:        print(f'Sorry there is not enough money. Money refunded.')        return False# 커피 만들고, 재료 차감 하기def makeCoffee(drink_name, drink_ingredients):    for item in drink_ingredients:        resources[item] -= drink_ingredients[item]    print(f'Here is your {drink_name}. Enjoy!')is_on = Truewhile is_on:    choice = input('What would you like? (espresso/latte/cappuccino): ')    if choice == 'off':        is_on = False    elif choice == 'report':        print(f'Water: {resources["water"]}')        print(f'Milk: {resources["milk"]}')        print(f'Coffee: {resources["coffee"]}')        print(f'Money: {profit}')    else:        drink = MENU[choice]        if checkResourceSufficient(drink['ingredients']):            payment = processCoins()            if isTransactionSuccessful(payment, drink['cost']):                makeCoffee(choice, drink['ingredients'])