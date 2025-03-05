# Loading and Examining the Image

Now that we have imported our libraries, we need to load the image that we want to overlay on our plot. Matplotlib provides some sample images that we can use for practice.

1. Create a new cell in your notebook and enter the following code:

```python
# Load the sample image
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)

# Display information about the image
print(f"Image shape: {im.shape}")
print(f"Image data type: {im.dtype}")

# Display the image
plt.figure(figsize=(4, 4))
plt.imshow(im)
plt.axis('off')  # Hide axis
plt.title('Matplotlib Logo')
plt.show()
```

This code does the following:

- Uses `cbook.get_sample_data()` to load a sample image named 'logo2.png' from Matplotlib's sample data collection.
- Uses `image.imread()` to read the image file into a NumPy array.
- Prints information about the image dimensions and data type.
- Creates a figure and displays the image using `plt.imshow()`.
- Hides the axis ticks and labels with `plt.axis('off')`.
- Adds a title to the figure.
- Displays the figure using `plt.show()`.

2. Run the cell by pressing Shift+Enter.

The output should display information about the image and show the Matplotlib logo. The image shape indicates the dimensions of the image (height, width, color channels), and the data type tells us how the image data is stored.

This step is important because it helps us understand the image we'll be using as an overlay. We can see its appearance and dimensions, which will be useful when deciding how to position it on our plot.
