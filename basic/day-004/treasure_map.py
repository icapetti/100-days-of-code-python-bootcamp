treasure_map = [
    ['⬜️', '⬜️', '⬜️'],
    ['⬜️', '⬜️', '⬜️'],
    ['⬜️', '⬜️', '⬜️']
]

print(f"{treasure_map[0]}\n{treasure_map[1]}\n{treasure_map[2]}")

position = input("Where do you want to put the treasure? ")
treasure_map[int(position[1])-1][int(position[0])-1] = '💰'

print("Your treasure has been successfully saved!")
print(f"{treasure_map[0]}\n{treasure_map[1]}\n{treasure_map[2]}")
