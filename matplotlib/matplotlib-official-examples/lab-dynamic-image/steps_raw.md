# Matplotlib Animation Lab

## Introduction

In this lab, we will learn how to create an animated image using precomputed lists of images. We will be using the Matplotlib library in Python to create the animation. The purpose of this lab is to demonstrate the process of creating an animated image and to provide a basic understanding of how it works.

## Steps

### Step 1: Import Libraries

To start, we need to import the libraries that we will be using. We will be using the Matplotlib library to create the animation and the Numpy library to generate the data for the animation.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
```

### Step 2: Create the Figure and Axes Objects

Next, we need to create the figure and axes objects that we will be using to create the animation. We will be using the subplots method to create these objects.

```python
fig, ax = plt.subplots()
```

### Step 3: Define the Function

We now need to define the function that we will be using to generate the data for the animation. In this example, we will be using the sine and cosine functions to generate the data.

```python
def f(x, y):
    return np.sin(x) + np.cos(y)
```

### Step 4: Generate the Data

We will be using the linspace method from the Numpy library to generate the data for the animation. We will be generating two sets of data, x and y, and then reshaping the y data to create a two-dimensional array.

```python
x = np.linspace(0, 2 * np.pi, 120)
y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
```

### Step 5: Create the Animation Frames

We will now create the frames for the animation. We will be using a for loop to generate 60 frames. In each iteration of the loop, we will be updating the x and y data and then creating a new image object using the imshow method. We will then append the image object to the ims list.

```python
ims = []
for i in range(60):
    x += np.pi / 15
    y += np.pi / 30
    im = ax.imshow(f(x, y), animated=True)
    if i == 0:
        ax.imshow(f(x, y))  # show an initial one first
    ims.append([im])
```

### Step 6: Create the Animation

We will now create the animation using the ArtistAnimation method. We will be passing in the figure object, the ims list, the interval between frames, and the repeat delay.

```python
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
```

### Step 7: Display the Animation

Finally, we will use the show method to display the animation.

```python
plt.show()
```

## Summary

In this lab, we learned how to create an animated image using precomputed lists of images. We used the Matplotlib library in Python to create the animation and the Numpy library to generate the data for the animation. We created the figure and axes objects, defined the function, generated the data, created the animation frames, and created the animation. We then displayed the animation using the show method. This lab provided a basic understanding of how to create an animated image and demonstrated the process of doing so.
