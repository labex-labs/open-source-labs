# Matplotlib Affine Transformation Lab

## Introduction

This lab demonstrates how to use Matplotlib to perform affine transformation of an image. Affine transformations change the shape and orientation of an image. This lab shows how to use the `transforms.Affine2D` function to manipulate the shape and orientation of an image.

## Steps

### Step 1: Import Libraries and Define the Image

In the first step, we import the necessary libraries and define the image that will be used in the example. The image is a combination of two Gaussian functions.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.transforms as mtransforms

def get_image():
    delta = 0.25
    x = y = np.arange(-3.0, 3.0, delta)
    X, Y = np.meshgrid(x, y)
    Z1 = np.exp(-X**2 - Y**2)
    Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
    Z = (Z1 - Z2)
    return Z
```

### Step 2: Create a Function to Plot the Image

In this step, we define a function that takes the image, the plot axis, and the transformation as inputs. The function displays the image on the plot axis with the specified transformation. The function also displays a yellow rectangle around the image to show the intended extent of the image.

```python
def do_plot(ax, Z, transform):
    im = ax.imshow(Z, interpolation='none',
                   origin='lower',
                   extent=[-2, 4, -3, 2], clip_on=True)

    trans_data = transform + ax.transData
    im.set_transform(trans_data)

    # display intended extent of the image
    x1, x2, y1, y2 = im.get_extent()
    ax.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1], "y--",
            transform=trans_data)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-4, 4)
```

### Step 3: Perform Image Rotation

In this step, we perform a rotation of the image using the `rotate_deg` function. We pass the rotation angle as the input to the `rotate_deg` function. We use the `do_plot` function to display the rotated image.

```python
# prepare image and figure
fig, ax1 = plt.subplots()
Z = get_image()

# image rotation
do_plot(ax1, Z, mtransforms.Affine2D().rotate_deg(30))
```

### Step 4: Perform Image Skew

In this step, we perform a skew of the image using the `skew_deg` function. We pass the skew angles as inputs to the `skew_deg` function. We use the `do_plot` function to display the skewed image.

```python
# prepare image and figure
fig, ax2 = plt.subplots()
Z = get_image()

# image skew
do_plot(ax2, Z, mtransforms.Affine2D().skew_deg(30, 15))
```

### Step 5: Perform Image Scale and Reflection

In this step, we perform a scale and reflection of the image using the `scale` function. We pass the scale and reflection factors as inputs to the `scale` function. We use the `do_plot` function to display the scaled and reflected image.

```python
# prepare image and figure
fig, ax3 = plt.subplots()
Z = get_image()

# scale and reflection
do_plot(ax3, Z, mtransforms.Affine2D().scale(-1, .5))
```

### Step 6: Perform Multiple Transformations

In this step, we perform multiple transformations of the image using the `rotate_deg`, `skew_deg`, `scale`, and `translate` functions. We pass the transformation parameters as inputs to the respective functions. We use the `do_plot` function to display the transformed image.

```python
# prepare image and figure
fig, ax4 = plt.subplots()
Z = get_image()

# everything and a translation
do_plot(ax4, Z, mtransforms.Affine2D().
        rotate_deg(30).skew_deg(30, 15).scale(-1, .5).translate(.5, -1))
```

## Summary

This lab demonstrated how to use Matplotlib to perform affine transformation of an image. We used the `transforms.Affine2D` function to manipulate the shape and orientation of an image. We performed rotation, skew, scale, reflection, and multiple transformations of the image. We also displayed the transformed image on a plot axis with the intended extent of the image.
