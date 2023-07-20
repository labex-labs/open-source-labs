# Animated Line Plot Tutorial

## Introduction

This tutorial will guide you through the process of creating an animated line plot using Python Matplotlib library. The line plot will display a sine wave with a changing amplitude over time.

## Steps

### Step 1: Import Libraries

The first step is to import the necessary libraries. We will be using Matplotlib for creating the plot and NumPy for generating data.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
```

### Step 2: Initialize the Figure and Axes

Next, we need to initialize the figure and axes for the plot. This can be done using the `subplots()` function from Matplotlib.

```python
fig, ax = plt.subplots()
```

### Step 3: Generate Data

In this step, we will generate the data for the line plot. We will be using the NumPy `arange()` function to generate an array of values for the x-axis, and the `sin()` function to generate an array of y-axis values for a sine wave.

```python
x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))
```

### Step 4: Define the Animation Function

The animation function will be called by the `FuncAnimation()` function and will be used to update the plot with new data. In this example, we will be updating the y-axis values of the line plot with a sine wave that has a changing amplitude over time.

```python
def animate(i):
    line.set_ydata(np.sin(x + i / 50))  # update the data.
    return line,
```

### Step 5: Create the Animation Object

Now we can create the animation object using the `FuncAnimation()` function. We will pass in the figure object, the animation function, the update interval, and the number of frames to be saved.

```python
ani = animation.FuncAnimation(
    fig, animate, interval=20, blit=True, save_count=50)
```

### Step 6: Display the Plot

Finally, we can display the plot using the `show()` function from Matplotlib.

```python
plt.show()
```

## Summary

In this tutorial, we have learned how to create an animated line plot using Python Matplotlib library. We have initialized the figure and axes, generated data, defined the animation function, and created the animation object. We have then displayed the plot using the `show()` function.
