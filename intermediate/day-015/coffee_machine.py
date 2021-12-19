from coffee_machine_aux import MENU, COINS

def get_user_order(user_choice: str) -> dict:
    """
    Ask user to input order.
    """
    if user_choice in MENU:
        return MENU[user_choice]

    else:
        print("Sorry, we don't have this item in our menu.")

def check_resources(resources: dict, order_ingredients: dict) -> bool:
    """
    Check if user has enough resources to make the order.
    """
    for ingredient, quantity in order_ingredients.items():
        if resources[ingredient] < quantity:
            return False

    return True

def calculate_change(user_order: dict, user_money: list) -> int:
    """
    Calculate change for the user.
    """
    total_paid = 0
    for coin, quantity in user_money.items():
        total_paid += quantity * COINS[coin]

    change = total_paid - user_order["cost"]
    return change

def update_resources(resources: dict, order_ingredients: dict) -> dict:
    """
    Update resources after user order.
    """
    for ingredient, quantity in order_ingredients.items():
        resources[ingredient] -= quantity

    return resources

def print_resources_report(resources: dict) -> None:
    """
    Print resources report.
    """
    for resource, quantity in resources.items():
        print(f"{resource}: {quantity}")

def main():
    on = True
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

    while on:
        user_choice = input("Enter with yout request (espresso, latte or cappuccino): ").lower()
        if user_choice == "report":
            print_resources_report(resources)

        elif user_choice == "off":
            print("Turning off the coffee machine. Bye!")
            on = False

        else:
            order = get_user_order(user_choice=user_choice)
            if not order:
                print("No order selected.")
                exit()

            if not check_resources(resources=resources, order_ingredients=order['ingredients']):
                print("Sorry, not enough resources.")
                exit()

            print(f"Your order costs {order['cost']}. Enter the coins: ")
            payment = {}
            for coin in COINS.keys():
                quantity = int(input(f"{coin}: "))
                payment[coin] = quantity

            change = calculate_change(user_order=order, user_money=payment)

            if change < 0:
                print("Sorry, not enough money.")
                exit()

            else:
                print(f"Your change is {change}.")

            resources = update_resources(resources=resources, order_ingredients=order['ingredients'])
            print("Enjoy your drink!")

if __name__ == '__main__':
    main()
