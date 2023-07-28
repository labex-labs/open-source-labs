# Animated Histogram Using Matplotlib

## Introduction

In this lab, you will learn how to create an animated histogram using Matplotlib in Python. The animated histogram will simulate new data coming in and update the heights of rectangles with the new data.

## Steps

### Step 1: Import Libraries

First, we need to import the necessary libraries.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
```

### Step 2: Set Random Seed and Bins

Set random seed for reproducibility and fix the bin edges.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# Fixing bin edges
HIST_BINS = np.linspace(-4, 4, 100)
```

### Step 3: Create Data and Histogram

Create data and histogram using NumPy.

```python
# histogram our data with numpy
data = np.random.randn(1000)
n, _, _ = plt.hist(data, HIST_BINS, lw=1, ec="yellow", fc="green", alpha=0.5)
```

### Step 4: Create Animation Function

We need to create an `animate` function that generates new random data and updates the heights of rectangles.

```python
def animate(frame_number):
    # simulate new data coming in
    data = np.random.randn(1000)
    n, _ = np.histogram(data, HIST_BINS)
    for count, rect in zip(n, bar_container.patches):
        rect.set_height(count)
    return bar_container.patches
```

### Step 5: Create Bar Container and Animation

Using `plt.hist` allows us to get an instance of `BarContainer`, which is a collection of `Rectangle` instances. We use `FuncAnimation` to setup the animation.

```python
# Using plt.hist allows us to get an instance of BarContainer, which is a
# collection of Rectangle instances. Calling prepare_animation will define
# animate function working with supplied BarContainer, all this is used to setup FuncAnimation.
fig, ax = plt.subplots()
_, _, bar_container = ax.hist(data, HIST_BINS, lw=1, ec="yellow", fc="green", alpha=0.5)
ax.set_ylim(top=55)  # set safe limit to ensure that all data is visible.

ani = animation.FuncAnimation(fig, animate, 50, repeat=False, blit=True)
plt.show()
```

## Summary

In this lab, you learned how to create an animated histogram using Matplotlib in Python. You started by importing the necessary libraries, setting random seed and bins, creating data and histogram, creating an animation function, and finally creating bar container and animation. By following these steps, you can create animated histograms to visualize data in a dynamic way.
