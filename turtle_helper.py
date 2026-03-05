import turtle

s = turtle.getscreen()

t = turtle.Turtle() # starts at right:

size = t.turtlesize()
increase = (2 * num for num in size)
t.turtlesize(*increase)

t.pensize(5)
t.shapesize()
t.pencolor("blue")

# Turn to the Right
def go_right():
    # target = 0
    current = round(t.heading())
    if current == 0:
        pass
    elif current == 90:
        t.right(90)
    elif current == 180:
        t.right(180)
    elif current == 270:
        t.left(90)
    else:
        raise ValueError('not a right angle!')
        
# Turn upwards
def go_up():
    # target = 90
    current = round(t.heading())
    if current == 0:
        t.left(90)
    elif current == 90:
        pass
    elif current == 180:
        t.right(90)
    elif current == 270:
        t.left(180)
    else:
        raise ValueError('not a right angle!')
        
# Turn to the left    
def go_left():
    # target = 180
    current = round(t.heading())
    if current == 0:
        t.left(180)
    elif current == 90:
        t.left(90)
    elif current == 180:
        pass
    elif current == 270:
        t.right(90)
    else:
        raise ValueError('not a right angle!')

# Turn downward
def go_down():
    # target = 270
    current = round(t.heading())
    if current == 0:
        t.right(90)
    elif current == 90:
        t.right(180)
    elif current == 180:
        t.left(90)
    elif current == 270:
        pass
    else:
        raise ValueError('not a right angle!')
        
# Move the object based on the command
def move_turtle(command):
    if command == 'up':
        go_up()
    elif command == 'down':
        go_down()
    elif command == 'left':
        go_left()
    elif command == 'right':
        go_right()
    elif command == 'go' or command == 'yes':
        t.forward(50)
    elif command == 'stop':
        print('Stopping the turtle')
