from turtle import Turtle, Screen

# Jimmy is an object of the Turtle class. 
# Which means it's an instance of the class Turtle.
jimmy = Turtle()

# shape is a method of the Turtle class that changes shape attribute of the object.
jimmy.shape("turtle")
jimmy.color("DarkGreen")
jimmy.forward(100)

my_screen = Screen()

# canvheight and canvwidth are attributes of the Screen class.
print(my_screen.canvheight)

# exitonclick is a method of the Screen class.
my_screen.exitonclick()
