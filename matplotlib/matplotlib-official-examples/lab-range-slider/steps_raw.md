# Thresholding an Image with RangeSlider

## Introduction

This lab will demonstrate how to use the RangeSlider widget in Matplotlib to control the thresholding of an image. The purpose of thresholding is to convert a grayscale image into a binary image, where the pixels are either black or white. This is useful for image segmentation, where we want to extract certain features from the image.

## Steps

### Step 1: Generate a fake image

First, we will generate a fake grayscale image using NumPy's random module. We will set the seed to ensure that the results are reproducible.

```python
np.random.seed(19680801)
N = 128
img = np.random.randn(N, N)
```

### Step 2: Display the image and its histogram

Next, we will display the image using Matplotlib's `imshow` function, and its histogram using `hist`. We will create a figure with two subplots, one for the image and one for the histogram.

```python
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
fig.subplots_adjust(bottom=0.25)

im = axs[0].imshow(img)
axs[1].hist(img.flatten(), bins='auto')
axs[1].set_title('Histogram of pixel intensities')
```

### Step 3: Create the RangeSlider

We will now create the RangeSlider widget, which will allow us to adjust the threshold of the image. We will create a new axis for the slider and add it to the figure.

```python
slider_ax = fig.add_axes([0.20, 0.1, 0.60, 0.03])
slider = RangeSlider(slider_ax, "Threshold", img.min(), img.max())
```

### Step 4: Add vertical lines to the histogram

To make it easier to see the effect of the thresholding, we will add vertical lines to the histogram to indicate the current threshold values. We will create two lines for the lower and upper threshold values, respectively.

```python
lower_limit_line = axs[1].axvline(slider.val[0], color='k')
upper_limit_line = axs[1].axvline(slider.val[1], color='k')
```

### Step 5: Create a callback function for the slider

We will create a callback function that will be called whenever the user changes the threshold values using the slider. The function will update the image's colormap and the positions of the vertical lines on the histogram.

```python
def update(val):
    # The val passed to a callback by the RangeSlider will
    # be a tuple of (min, max)

    # Update the image's colormap
    im.norm.vmin = val[0]
    im.norm.vmax = val[1]

    # Update the position of the vertical lines
    lower_limit_line.set_xdata([val[0], val[0]])
    upper_limit_line.set_xdata([val[1], val[1]])

    # Redraw the figure to ensure it updates
    fig.canvas.draw_idle()


slider.on_changed(update)
```

### Step 6: Display the figure

Finally, we will display the figure with the image and the slider.

```python
plt.show()
```

## Summary

In this lab, we have demonstrated how to use the RangeSlider widget in Matplotlib to control the thresholding of an image. We have shown how to create a fake grayscale image, display it and its histogram, create a slider to adjust the threshold values, and update the image and histogram based on the slider values. This technique can be used for image segmentation and other applications where we need to extract certain features from an image.
