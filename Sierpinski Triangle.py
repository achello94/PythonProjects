import turtle

wn = turtle.Screen ( )
wn.bgcolor("GREEN")
alex = turtle.Turtle ( )
alex.speed(speed=0)

alex.color("yellow")
alex.pensize(2)

x = 100
z = 100

count = 0

#LETS START WITH THE FIRST ITERATION OF THE TRIANGLE

#This is a way to move the turtle to the appropriate position using conditionals
first = range(1, 40, 3)
second = range(2, 41, 3)
third = range(3, 42, 3)

for i in range (2, 6):
    # External Triangle
    alex.forward (x)
    alex.left (120)
    alex.forward (x)
    alex.left (120)
    alex.forward (x)
    alex.left (120)

    # First Triangle
    alex.forward (x / 2)
    alex.left (120)
    alex.forward (x / 2)
    alex.left (120)
    alex.forward (x / 2)
    alex.left (120)

    # Second Triangle
    alex.forward (x / 1)
    alex.left (120)
    alex.forward (x / 2)
    alex.left (120)
    alex.forward (x / 2)
    alex.left (120)

    #Third Triangle
    alex.forward (x / 2)
    alex.left (120)
    alex.forward (x / 1)
    alex.left (120)
    alex.forward (x / 2)
    alex.left (120)

    # Back to Initial Position
    alex.forward (x / 2)
    alex.left (120)
    alex.forward (x / 2)
    alex.left (120)
    alex.forward (x / 1)
    alex.left (120)

    if count in third:
        alex.right (120)
        alex.forward (x)
        alex.left (120)

    #Increase the counter for the number of iterations
    count +=1


    
    if count in first:
        x = x / 2

        if count ==7:
            alex.forward(100)
            x = x*2

    elif count in second:
        alex.forward(x)

    elif count in third:

        if count == 10:
            x = x *10
        else:
            pass

        alex.forward(x)
        alex.left (120)
        alex.forward (x*2)
        alex.left (120)
        alex.forward (x)
        alex.left (120)


#SECOND ITERATION OF THE TRIANGLE

alex.penup()
alex.goto(-z,0)
alex.pendown()

x = z
count = 0

#This is a way to move the turtle to the appropriate position using conditionals
first = range(1, 40, 3)
second = range(2, 41, 3)
third = range(3, 42, 3)

for i in range (2, 6):
    # External Triangle
    alex.forward (x)
    alex.left (120)
    alex.forward (x)
    alex.left (120)
    alex.forward (x)
    alex.left (120)

    # First Triangle
    alex.forward (x / 2)
    alex.left (120)
    alex.forward (x / 2)
    alex.left (120)
    alex.forward (x / 2)
    alex.left (120)

    # Second Triangle
    alex.forward (x / 1)
    alex.left (120)
    alex.forward (x / 2)
    alex.left (120)
    alex.forward (x / 2)
    alex.left (120)

    #Third Triangle
    alex.forward (x / 2)
    alex.left (120)
    alex.forward (x / 1)
    alex.left (120)
    alex.forward (x / 2)
    alex.left (120)

    # Back to Initial Position
    alex.forward (x / 2)
    alex.left (120)
    alex.forward (x / 2)
    alex.left (120)
    alex.forward (x / 1)
    alex.left (120)

    if count in third:
        alex.right (120)
        alex.forward (x)
        alex.left (120)

    #Increase the counter for the number of iterations
    count +=1


    
    if count in first:
        x = x / 2

        if count ==7:
            alex.forward(100)
            x = x*2

    elif count in second:
        alex.forward(x)

    elif count in third:

        if count == 10:
            x = x *10
        else:
            pass

        alex.forward(x)
        alex.left (120)
        alex.forward (x*2)
        alex.left (120)
        alex.forward (x)
        alex.left (120)

#THIRD ITERATION OF THE TRIANGLE

alex.penup()
alex.goto(-z/2,+z*(1-0.12))
alex.pendown()

x = z
count = 0

#This is a way to move the turtle to the appropriate position using conditionals
first = range(1, 40, 3)
second = range(2, 41, 3)
third = range(3, 42, 3)

for i in range (2, 6):
    # External Triangle
    alex.forward (x)
    alex.left (120)
    alex.forward (x)
    alex.left (120)
    alex.forward (x)
    alex.left (120)

    # First Triangle
    alex.forward (x / 2)
    alex.left (120)
    alex.forward (x / 2)
    alex.left (120)
    alex.forward (x / 2)
    alex.left (120)

    # Second Triangle
    alex.forward (x / 1)
    alex.left (120)
    alex.forward (x / 2)
    alex.left (120)
    alex.forward (x / 2)
    alex.left (120)

    #Third Triangle
    alex.forward (x / 2)
    alex.left (120)
    alex.forward (x / 1)
    alex.left (120)
    alex.forward (x / 2)
    alex.left (120)

    # Back to Initial Position
    alex.forward (x / 2)
    alex.left (120)
    alex.forward (x / 2)
    alex.left (120)
    alex.forward (x / 1)
    alex.left (120)

    if count in third:
        alex.right (120)
        alex.forward (x)
        alex.left (120)

    #Increase the counter for the number of iterations
    count +=1


    
    if count in first:
        x = x / 2

        if count ==7:
            alex.forward(100)
            x = x*2

    elif count in second:
        alex.forward(x)

    elif count in third:

        if count == 10:
            x = x *10
        else:
            pass

        alex.forward(x)
        alex.left (120)
        alex.forward (x*2)
        alex.left (120)
        alex.forward (x)
        alex.left (120)



wn.exitonclick()


