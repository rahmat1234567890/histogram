from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import filedialog

def calculate_color_histogram(image_path):
    # Load the image
    image = Image.open(image_path)
    rgb_image = image.convert('RGB')

    # Get the size of the image
    width, height = image.size


    # Convert the image to a list of pixels
    pixels = list(rgb_image.getdata())

    # Calculate the size of each RGB color component
    red_size = 0
    green_size = 0
    blue_size = 0

    # Calculate the histogram bins
    # bins = list(range(256))

    # Iterate over each pixel
    for pixel in pixels:
        red_value, green_value, blue_value = pixel

        # Accumulate the color component sizes
        red_size += red_value
        green_size += green_value
        blue_size += blue_value

    # Calculate the percentage of each color component
    total_size = red_size + green_size + blue_size
    red_percentage = (red_size / total_size) * 100
    green_percentage = (green_size / total_size) * 100
    blue_percentage = (blue_size / total_size) * 100

    # Calculate the color histograms
    red_hist = [0] * 256
    green_hist = [0] * 256
    blue_hist = [0] * 256

    # Iterate over each pixel again to build the histograms
    for pixel in pixels:
        red_value, green_value, blue_value = pixel

        # Increment the corresponding histogram bin
        red_hist[red_value] += 1
        green_hist[green_value] += 1
        blue_hist[blue_value] += 1

    # Convert the image to a matrix
    image_matrix = np.array(rgb_image)
        

# # Print the resulting matrix


    return (
        red_size,
        green_size,
        blue_size,
        red_percentage,
        green_percentage,
        blue_percentage,
        image_matrix,
        red_hist,
        green_hist,
        blue_hist,
    )


def open_image():
    root = tk.Tk()
    root.withdraw()
    image_path = filedialog.askopenfilename(title="Select Image")
    return image_path


# Open the image
image_path = open_image()

# Calculate color histogram and get the sizes, percentages, image, and histograms
red_size, green_size, blue_size, red_percentage, green_percentage, blue_percentage, image_matrix, red_hist, green_hist, blue_hist = calculate_color_histogram(
    image_path
)

# Print the color sizes and percentages
print(f"Red Size: {red_size}")
print(f"Green Size: {green_size}")
print(f"Blue Size: {blue_size}")
print(f"Red Percentage: {red_percentage:2f}%")
print(f"Green Percentage: {green_percentage:.2f}%")
print(f"Blue Percentage: {blue_percentage:.2f}%")

# Show the image
image = Image.fromarray(image_matrix)
image.show()

# Plot the color histogram
plt.figure(figsize=(10, 6))
plt.plot(red_hist, color="red", label="Red")
plt.plot(green_hist, color="green", label="Green")
plt.plot(blue_hist, color="blue", label="Blue")
plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.title("Color Histogram")
plt.legend()
plt.show()
print(image_matrix)
