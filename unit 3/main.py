import turtle as trtl

# Create the main game window and set the background image
wn = trtl.Screen()
wn.tracer(False)
wn.addshape("./unit 3/images/resized_red_piece.gif")
wn.addshape("./unit 3/images/resized_black_piece.gif")

# Set up the Turtle screen
screen = trtl.Screen()
screen.setup(800, 800)
screen.bgcolor("white")

# Create a Turtle object for the checkerboard
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
        piece.shape("./unit 3/images/resized_red_piece.gif")
    elif color == "black":
        piece.shape("./unit 3/images/resized_black_piece.gif")
    piece.penup()
    piece.goto(x, y)
    pieces.append((piece, color, (x, y)))

# Function to move a checkers piece turtle to a new position
def move_checkers_piece(piece, x, y):
    # Calculate the center of the grid square that corresponds to the new position
    new_x = ((x // 100) * 100) + 50
    new_y = ((y // 100) * 100) + 50
    piece.goto(new_x, new_y)

# Function to check if a move is valid
def is_valid_move(piece, new_x, new_y, color):
    if piece is None:
        return False
    # Calculate the current position of the piece
    piece_x, piece_y = piece.pos()
    # Calculate the difference between the current position and the new position
    dx = new_x - piece_x
    dy = new_y - piece_y

    # Check if the move is diagonal and empty
    if abs(dx) in range(50, 150) and abs(dy) in range(50, 150):
        # Calculate the position that the piece is moving to
        new_x = ((new_x // 100) * 100) + 50
        new_y = ((new_y // 100) * 100) + 50
        new_pos = (new_x, new_y)

        # Check if the new position is empty (i.e., no other piece is there)
        for other_piece, _, pos in pieces:
            if pos == new_pos:
                print("Invalid move: The selected space is already occupied")
                return False

        # Check if the color of the piece matches the player's turn
        if color == "black" and new_y <= piece_y:
            print("Invalid move: Black piece can't move backward")
            return False

        if color == "red" and new_y >= piece_y:
            print("Invalid move: Red piece can't move backward")
            return False

        return True
    else:
        return False

# Function to handle mouse clicks
def on_click(x, y):
    global selected_piece, selected_piece_pos, selected_piece_color, current_turn
    if selected_piece is None:
        # Check if a piece was clicked
        for piece, color, pos in pieces:
            piece_x, piece_y = pos
            distance = ((x - piece_x) ** 2 + (y - piece_y) ** 2) ** 0.5
            if distance < 60:
                if current_turn == color:
                    selected_piece = piece
                    selected_piece_pos = pos
                    selected_piece_color = color
                    print(f"Selected piece: {color} at position {pos}")
                else:
                    print(f"Player clicked on a {color} piece on {current_turn}'s turn")
                break
    else:
        # Check if the clicked square is valid for a move
        valid_move = is_valid_move(selected_piece, x, y, selected_piece_color)

        if valid_move:
            move_x = ((x // 100) * 100) + 50
            move_y = ((y // 100) * 100) + 50
            move_checkers_piece(selected_piece, move_x, move_y)
            piece_index = None
            for index, (_, _, pos) in enumerate(pieces):
                if pos == selected_piece_pos:
                    piece_index = index
                    break
            if piece_index is not None:
                fix_x = ((move_x // 100) * 100) + 50
                fix_y = ((move_y // 100) * 100) + 50
                pieces[piece_index] = (selected_piece, selected_piece_color, (fix_x, fix_y))

            selected_piece = None
            selected_piece_pos = None
            switch_turn()
        else:
            # Deselect the piece if the click was not valid
            selected_piece = None
            selected_piece_pos = None

# Function to switch the turn to the other player
def switch_turn():
    global current_turn
    if current_turn == "red":
        current_turn = "black"
    else:
        current_turn = "red"

# Function to check if a capture move is valid
def is_valid_capture(piece, new_x, new_y, color):
    if piece is None:
        return False
    # Calculate the current position of the piece
    piece_x, piece_y = piece.pos()
    # Calculate the difference between the current position and the new position
    dx = new_x - piece_x
    dy = new_y - piece_y

    # Check if the move is diagonal and empty
    if abs(dx) in range(50, 150) and abs(dy) in range(50, 150):
        # Calculate the position that the piece is moving to
        new_x = ((new_x // 100) * 100) + 50
        new_y = ((new_y // 100) * 100) + 50
        new_pos = (new_x, new_y)

        # Check if the new position is empty (i.e., no other piece is there)
        for other_piece, _, pos in pieces:
            if pos == new_pos:
                return False

        # Calculate the position of the piece to be captured
        captured_x = piece_x + (dx // 2)
        captured_y = piece_y + (dy // 2)
        captured_pos = (captured_x, captured_y)

        # Check if there is an opponent's piece to be captured
        for opp_piece, opp_color, opp_pos in pieces:
            if opp_pos == captured_pos and opp_color != color:
                return True

    return False

# Function to capture an opponent's piece
def capture_piece(selected_piece, capture_piece_at):
    # Find and remove the captured piece from the pieces list
    for index, (piece, color, pos) in enumerate(pieces):
        if pos == capture_piece_at:
            pieces.pop(index)
            piece.hideturtle()
            print(f"Piece captured at {capture_piece_at}")

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
selected_piece_color = None

# Register the click handler
wn.onclick(on_click)

# Initialize the turn variable
current_turn = "black"  # Start with black's turn

# Keep the window open
wn.mainloop()