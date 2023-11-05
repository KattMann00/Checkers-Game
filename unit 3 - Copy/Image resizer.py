from PIL import Image

# Open the image
image = Image.open("checkerboard.png")

# Resize the image to the desired width and height
new_width = 800  # Replace with your desired width
new_height = 800  # Replace with your desired height
resized_image = image.resize((new_width, new_height))

# Save the resized image
resized_image.save("resized_checkerboard.png")