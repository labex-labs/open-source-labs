# Python Matplotlib Animated Scatter Plot Lab

## Introduction

This lab is designed to teach you how to create an animated scatter plot using Python's Matplotlib library. We will cover everything from setting up the plot to saving the animation as a GIF. By the end of this lab, you will have a working animated scatter plot that you can use to visualize your data.

## Steps

### Step 1: Setting up the Plot

The first step in creating an animated scatter plot is to set up the plot itself. This involves importing the necessary libraries and creating a figure and axes object.

```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
```

### Step 2: Defining the Data

Next, we need to define the data that we will be using for our scatter plot. In this example, we will be using a simple array of numbers ranging from 0 to 10.

```python
x = np.linspace(0, 10)
```

### Step 3: Creating the Scatter Plot

Now that we have our data, we can create the scatter plot. We do this by calling the scatter function on our axes object and passing in our x data.

```python
scat = ax.scatter(1, 0)
```

### Step 4: Creating the Animation

The final step is to create the animation. We do this using the FuncAnimation function from the animation module. This function takes a few arguments, including the figure object, the function that will update the plot, and the number of frames to use.

```python
def animate(i):
    scat.set_offsets((x[i], 0))
    return scat,

ani = animation.FuncAnimation(fig, animate, repeat=True,
                                    frames=len(x) - 1, interval=50)
```

### Step 5: Displaying the Plot

We can now display the plot by calling the show function from the pyplot module.

```python
plt.show()
```

## Summary

In this lab, we learned how to create an animated scatter plot using Python's Matplotlib library. We covered everything from setting up the plot to saving the animation as a GIF. With this knowledge, you can now create your own animated scatter plots to visualize your data.
