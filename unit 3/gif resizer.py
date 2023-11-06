from PIL import Image

# Open the GIF
gif_path = "./images/red king.gif"
original_gif = Image.open(gif_path)

# Get the number of frames in the GIF
num_frames = original_gif.n_frames

# Create a list to store the resized frames
resized_frames = []

# Define the desired width and height
new_width = 50
new_height = 50

# Loop through each frame and resize it
for frame in range(num_frames):
    original_gif.seek(frame)
    frame_image = original_gif.copy()
    frame_image = frame_image.resize((new_width, new_height), Image.ANTIALIAS)
    resized_frames.append(frame_image)

# Save the resized frames as a new GIF
output_gif_path = "resized_red_king.gif"
resized_frames[0].save(
    output_gif_path,
    save_all=True,
    append_images=resized_frames[1:],
    duration=original_gif.info['duration'],
    loop=0  # 0 means an infinite loop; change as needed
)
