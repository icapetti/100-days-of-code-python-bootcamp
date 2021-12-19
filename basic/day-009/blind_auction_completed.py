from helper import logo

print(logo)
print("Welcome to the secret auction program.")

names_and_bids = {}
get_bid = True
while get_bid:
    name = input("What's your name? ").title()
    bid = float(input("What's your bid? $"))
    names_and_bids[name] = bid

    should_continue = input("Are there any other bidders? y/n: ").lower()
    get_bid = False if should_continue == 'n' else True

highest_bid = max(names_and_bids, key=names_and_bids.get)
print(f"The winner is {highest_bid} with a bid of ${names_and_bids[highest_bid]}.")
