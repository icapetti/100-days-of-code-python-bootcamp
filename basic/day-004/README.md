## Randomisation
Randomisation is really important when we want to create computer programs that have a degree of unpredictability. Tge biggest category of that is games. 

When we talk about computers, these machines are what we would call deterministic. They will perform repeatable actions in a fully predictable way. 

So, how do we wrangle these machines that operate basically on ones and zeros to get them to create some random numbers? 

There's a whole bunch of maths that can be applied to create what are called a pseudo-random number generators.

The one that Python uses is something called the Mersenne Twister. The module that in Python that implements the Mersenne Twister is `random`.

### Heads or Tails
You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
You should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

e.g.
1 means Heads
0 means Tails

### Who will pay the bill
You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

Example Input
Angela, Ben, Jenny, Michael, Chloe

Example Output
Michael is going to buy the meal today!

### Treasure map
You are going to write a program which will mark a spot with an X.

In the starting code, you will find a variable called map.

This map contains a nested list.
When map is printed this is what the nested list looks like:

['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']

In the starting code, we have used new lines (\n) to format the three rows into a square, like this:

['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']

This is to try and simulate the coordinates on a real map.

Your job is to write a program that allows you to mark a square on the map using a two-digit system. The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:

https://cdn.fs.teachablecdn.com/2vnboIYTFFruvl9FJ2w5

First your program must take the user input and convert it to a usable format.
Next, you need to use it to update your nested list with an "x".

Example Input 1
column 2, row 3 would be entered as:

23

Example Output 1
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', 'X', '⬜️']

