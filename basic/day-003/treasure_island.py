print(
"""
                             -|             |-
         -|                  [-_-_-_-_-_-_-_-]                  |-
         [-_-_-_-_-]          |             |          [-_-_-_-_-]
          | o   o |           [  0   0   0  ]           | o   o |
           |     |    -|       |           |       |-    |     |
           |     |_-___-___-___-|         |-___-___-___-_|     |
           |  o  ]              [    0    ]              [  o  |
           |     ]   o   o   o  [ _______ ]  o   o   o   [     | ----__________
_____----- |     ]              [ ||||||| ]              [     |
           |     ]              [ ||||||| ]              [     |
       _-_-|_____]--------------[_|||||||_]--------------[_____|-_-_
      ( (__________------------_____________-------------_________) )

Welcome to the mysterious castle.
Find an ancient treasure hidden in this castle if you can.
""")

step = input("You're at a crossroad. Where do you want to go? Type 'left'  or 'right' ").lower()
if step != "left":
    print("Fall into a hole. Game over!")
    exit()

print("You've come to a lake. \nThere is an island in the middle of the lake.")
step = input("Type 'wait' to wait for a boat. Type 'swim' to swim across. ").lower()
if step != "wait":
    print("You get attacked by an angry trout. Game Over!")
    exit()

print("You arrive at the island unharmed. \nThere is a house with 3 doors. One red, one yellow and one blue.")
step = input("Which colour do you choose? ").lower()
if step == "red":
    print("It's a room full of fire. Game Over!")
elif step == "blue":
    print("You enter a room of beasts. Game Over!")
elif step == "yellow":
    print("""

    You found the treasure! You Win!
                                        .''.       
        .''.      .        *''*    :_\/_:     . 
        :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
    .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
    :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
    : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
    '..'  ':::'     * /\ *     .'/.\'.   '
        *            *..*         :
    jgs     *
            *
    """)
else:
    print("You chose a door that doesn't exist. Game Over!")
