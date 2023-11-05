import turtle

# Create a turtle for drawing lines
drawing_turtle = turtle.Turtle()
drawing_turtle.penup()
drawing_turtle.speed(0)  # Set the drawing speed to the maximum
drawing_turtle.pensize(4)

def get_mouse_click_coor(x, y):
    # Format the coordinates as "(x, y)" and then print them
    formatted_coordinates = f"({x}, {y})"
    print(formatted_coordinates)
    
    drawing_turtle.goto(x, y)
    drawing_turtle.pendown()  # Put the pen down to draw a line

turtle.onscreenclick(get_mouse_click_coor)

wn = turtle.Screen()
picture = "resized_checkerboard.gif"
wn.addshape(picture)

# Set the main turtle's shape to the loaded image
turtle.shape(picture)

turtle.mainloop()