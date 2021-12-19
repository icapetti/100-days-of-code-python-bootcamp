from random import choice

from arts import logo, vs
from game_data import data

def get_item() -> dict:
    """"""
    return choice(data)

def get_jig(items: list) -> str:
    """"""
    value1 = items[-2]['follower_count']
    value2 = items[-1]['follower_count']

    if value1 > value2:
        return 'a'
    
    if value1 < value2:
        return 'b'

def check_answer(jig: str, answer: str) -> bool:
    """"""
    return True if jig == answer else False

def update_score(score: int) -> int:
    """"""
    return score + 1

def update_items(items: list, jig: str) -> list:
    """"""
    if jig == 'a':
        items[-1] = items[-2]

    new_item = get_item()
    while new_item in items:
        new_item = get_item()
    
    items.append(new_item)

    return items

def print_followers(items: list) -> None:
    """"""
    for item in items[-2:]:
        print(f'{item["name"]} has {item["follower_count"]} followers')

score = 0
play = True

print(logo)
print("Welcome to Higher or Lower game!")

items_to_compare = []
for _ in range(2):
    items_to_compare.append(get_item())

jig = get_jig(items=items_to_compare)

while play:
    print(f"\nCompare A: {items_to_compare[-2]['name']}, a {items_to_compare[-2]['description']} from {items_to_compare[-2]['country']}")
    print(vs)
    print(f"Compare B: {items_to_compare[-1]['name']}, a {items_to_compare[-1]['description']} from {items_to_compare[-1]['country']}\n")

    user_answer = input("Who has more followers? (A/B) ").lower()
    if check_answer(jig=jig, answer=user_answer):
        score = update_score(score=score)
        print(f"Correct! Your score is {score}")
        print_followers(items=items_to_compare)
        items_to_compare = update_items(items=items_to_compare, jig=jig)
        jig = get_jig(items=items_to_compare)

    else:
        print("Wrong!")
        print_followers(items=items_to_compare)
        play = False

print(f"\nYour final score is {score}")
    