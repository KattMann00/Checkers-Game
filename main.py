import turtle

def draw_square(color, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()

def draw_checker(x, y, color):
    turtle.penup()
    turtle.goto(x + 25, y - 25)  # Center the checker in the square
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(20)  # Radius of 20 for the checker size
    turtle.end_fill()

def draw_board():
    turtle.speed('fastest')  # Draw the board quickly
    turtle.tracer(0, 0)  # Turn off animation for instant drawing
    start_x = -200  # Starting x position of the board
    start_y = 200   # Starting y position of the board
    for row in range(8):
        for col in range(8):
            square_color = 'gray' if (row + col) % 2 == 0 else 'white'
            draw_square(square_color, start_x + col * 50, start_y - row * 50)
    turtle.update()  # Update the drawing once the entire board is drawn

def update_checkers():
    # Clear the turtle's drawings and redraw the board and checkers
    turtle.reset()  # This clears the drawing and resets the turtle state
    draw_board()    # Redraw the board
    draw_all_checkers()  # Draw all checkers at their new positions

def create_checker_positions():
    # Clear any existing checkers first
    checkers.clear()
    # Populate the checkers for the initial game setup
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 1:  # Checkers are placed on squares where row+col is odd
                if row < 3:  # The first three rows from the top
                    checkers[(col, row)] = 'black'  # Black checkers
                elif row > 4:  # The last three rows from the bottom
                    checkers[(col, row)] = 'red'  # Red checkers

def square_center(col, row):
    """Get the screen coordinates for the center of the square at (col, row)."""
    start_x = -200  # Starting x position of the board
    start_y = 200   # Starting y position of the board
    return (start_x + col * 50 + 25, start_y - row * 50 - 25)

def draw_all_checkers():
    for position, color in checkers.items():
        x, y = square_center(*position)
        draw_checker(x, y, color)

def select_checker(x, y):
    global selected_checker
    col = int((x + 200) // 50)
    row = int((200 - y) // 50)
    if (col, row) in checkers:
        selected_checker = (col, row)
    else:
        selected_checker = None

def move_checker(x, y):
    global selected_checker
    if selected_checker:
        col = int((x + 200) // 50)
        row = int((200 - y) // 50)
        target_pos = (col, row)
        if target_pos not in checkers and (col + row) % 2 == 1:
            is_king = 'K' in checkers[selected_checker]  # Check if the checker is a king
            if is_valid_move(selected_checker, target_pos, is_king):
                # Handle capture
                if abs(selected_checker[0] - col) == 2:
                    middle_col = (selected_checker[0] + col) // 2
                    middle_row = (selected_checker[1] + row) // 2
                    del checkers[(middle_col, middle_row)]  # Remove the captured piece

                # Move the checker
                checkers[target_pos] = checkers.pop(selected_checker)

                # Check for kingmaking
                if (checkers[target_pos] == 'red' and row == 0) or (checkers[target_pos] == 'black' and row == 7):
                    checkers[target_pos] += 'K'  # Append 'K' to denote a king

                selected_checker = None
                update_checkers()  # Update the checkers instead of redrawing the entire board

            else:
                print("Invalid move")
                # TODO: Provide feedback to the user about why the move is invalid

def click_handler(x, y):
    if selected_checker:
        move_checker(x, y)
    else:
        select_checker(x, y)

def is_valid_move(start_pos, end_pos, is_king):
    start_col, start_row = start_pos
    end_col, end_row = end_pos
    move_direction = 1 if checkers[start_pos] == 'red' else -1

    # Check if the move is diagonal
    if abs(start_col - end_col) == abs(start_row - end_row) == 1:
        # Regular move
        if (is_king or (end_row - start_row) == move_direction) and end_pos not in checkers:
            return True
    elif abs(start_col - end_col) == abs(start_row - end_row) == 2:
        # Jump move
        jumped_col = (start_col + end_col) // 2
        jumped_row = (start_row + end_row) // 2
        if (is_king or (end_row - start_row) == move_direction * 2) and end_pos not in checkers:
            if (jumped_col, jumped_row) in checkers and checkers[(jumped_col, jumped_row)] != checkers[start_pos]:
                return True
    return False

# Global variables to keep track of the game state
selected_checker = None
checkers = {}  # Initialize the dictionary

wn = turtle.Screen()
wn.title("Checkers")
wn.bgcolor("white")

create_checker_positions()  # Populate the checkers on the board

draw_board()  # Draw the checkerboard once

update_checkers()  # Draw all checkers at their starting positions

# Bind the click handler
turtle.onscreenclick(click_handler)

# Keep the window open
wn.mainloop()