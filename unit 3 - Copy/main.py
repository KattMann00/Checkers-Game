import turtle as trtl
import random as rand

# Create the main game window and set the background image
wn = trtl.Screen()
wn.tracer(False)
wn.addshape("resized_red_piece.gif")
wn.addshape("resized_black_piece.gif")

# Set up the Turtle screen
screen =trtl.Screen()
screen.setup(800, 800)
screen.bgcolor("white")
#ex comment
# Create a Turtle object
board = trtl.Turtle()
board.speed(0)  # Set the drawing speed (0 is the fastest)

# Function to draw a square
def draw_square(size, color):
    board.begin_fill()
    board.fillcolor(color)
    for _ in range(4):
        board.forward(size)
        board.right(90)
    board.end_fill()

# Set initial position
board.penup()
board.goto(-400, 400)
board.pendown()

# Define the checkerboard pattern
colors = ["black", "white"]
color_index = 0
square_size = 100

# Draw the checkerboard
for _ in range(8):
    for _ in range(8):
        draw_square(square_size, colors[color_index])
        board.forward(square_size)
        color_index = (color_index + 1) % 2
    board.backward(8 * square_size)
    board.right(90)
    board.forward(square_size)
    board.left(90)
    color_index = (color_index + 1) % 2
# Create a list to store the turtle objects for the checkers pieces and their positions
pieces = []

# Function to create a checkers piece turtle at a given position
def create_checkers_piece(x, y, color):
    piece = trtl.Turtle()
    piece.speed(0)
    if color == "red":
        piece.shape("resized_red_piece.gif")
    elif color == "black":
        piece.shape("resized_black_piece.gif")
    piece.penup()
    piece.goto(x, y)
    pieces.append((piece, color, (x, y)))

# Function to move a checkers piece turtle to a new position
def move_checkers_piece(piece, x, y):
    # Calculate the center of the grid square that corresponds to the new position
    print ("you clicked on ",  {x, y})
    new_x = ((x // 100) * 100) + 50
    new_y = ((y // 100) * 100) + 50
    piece.goto(new_x, new_y)
    print("turtle moved to ", {new_x, new_y})

# Function to check if a move is valid
def is_valid_move(piece, new_x, new_y):
    # Calculate the current position of the piece
    piece_x, piece_y = piece.pos()
    
    # Calculate the difference between the current position and the new position
    dx = new_x - piece_x
    dy = new_y - piece_y

    # Check if the move is diagonal and empty
    if abs(dx) in range (50,150) and abs(dy) in range (50,150):
        # Calculate the position that the piece is moving to
        new_pos = (new_x, new_y)
        
        # Check if the new position is empty (i.e., no other piece is there)
        for other_piece, _, pos in pieces:
            if pos == new_pos:
                print("piece already here")
                return False

        return True
    else:
        print("not valid space")
        return False


# Function to handle mouse clicks
# Function to handle mouse clicks
def on_click(x, y):
    global selected_piece, selected_piece_pos
    if selected_piece is None:
        # Check if a piece was clicked
        for index, (piece, color, pos) in enumerate(pieces):
            piece_x, piece_y = pos
            distance = ((x - piece_x) ** 2 + (y - piece_y) ** 2) ** 0.5
            if distance < 60:  # adjust this threshold as needed, 70 for corners
                selected_piece = piece
                selected_piece_pos = pos
                print(f"Selected piece: {color} at position {pos}")
                break
    elif is_valid_move(selected_piece, x, y):
        move_checkers_piece(selected_piece, x, y)
        # Find the index of the selected piece in the pieces list
        piece_index = None
        for index, (_, _, pos) in enumerate(pieces):
            if pos == selected_piece_pos:
                piece_index = index
                break

        if piece_index is not None:
            # Update the piece's position in the pieces list
            pieces[piece_index] = (selected_piece, selected_piece_pos[1], (x, y))
        
        selected_piece = None
        selected_piece_pos = None



# positions for pieces
positions = [(-350, 350, "red"), (-150, 350, "red"), (50, 350, "red"), (250, 350, "red"), (-250, 250, "red"), (-50, 250, "red"), (150, 250, "red"), (350, 250, "red"), 
             (-350, 150, "red"), (-150, 150, "red"), (50, 150, "red"), (250, 150, "red"), (-250, -350, "black"), (-50, -350, "black"), (150, -350, "black"), (350, -350, "black"), 
             (-350, -250, "black"), (-150, -250, "black"), (50, -250, "black"), (250, -250, "black"), (-250, -150, "black"), (-50, -150, "black"), (150, -150, "black"), (350, -150, "black")]

# Create checkers pieces and place them at the specified positions
for x, y, color in positions:
    create_checkers_piece(x, y, color)
wn.tracer(True)
# Initialize variables to keep track of the selected piece and its position
selected_piece = None
selected_piece_pos = None

# Register the click handler
wn.onclick(on_click)

# Keep the window open
wn.mainloop()