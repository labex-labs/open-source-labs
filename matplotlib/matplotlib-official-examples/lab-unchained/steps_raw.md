# Matplotlib Data Visualization Lab

## Introduction

This lab is designed to introduce you to the basics of data visualization using Matplotlib. Matplotlib is a popular data visualization library for Python that provides a wide range of options for creating plots, graphs, and charts.

## Steps

### Step 1: Setting Up

Before we start, we need to ensure that Matplotlib is installed. You can install it using pip, by running the following command:

```python
!pip install matplotlib
```

Once installed, we need to import the library and set up the environment:

```python
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

# Create new Figure with black background
fig = plt.figure(figsize=(8, 8), facecolor='black')

# Add a subplot with no frame
ax = plt.subplot(frameon=False)
```

### Step 2: Generating Random Data

In this step, we will generate random data that we will use to create our plot.

```python
# Generate random data
data = np.random.uniform(0, 1, (64, 75))
X = np.linspace(-1, 1, data.shape[-1])
G = 1.5 * np.exp(-4 * X ** 2)
```

### Step 3: Creating Line Plots

We will create line plots using the random data that we generated in the previous step.

```python
# Generate line plots
lines = []
for i in range(len(data)):
    # Small reduction of the X extents to get a cheap perspective effect
    xscale = 1 - i / 200.
    # Same for linewidth (thicker strokes on bottom)
    lw = 1.5 - i / 100.0
    line, = ax.plot(xscale * X, i + G * data[i], color="w", lw=lw)
    lines.append(line)
```

### Step 4: Setting Limits and Removing Ticks

In this step, we will set the y limit and remove the ticks from the plot.

```python
# Set y limit (or first line is cropped because of thickness)
ax.set_ylim(-1, 70)

# No ticks
ax.set_xticks([])
ax.set_yticks([])
```

### Step 5: Adding Title

We will add a title to our plot.

```python
# 2 part titles to get different font weights
ax.text(0.5, 1.0, "MATPLOTLIB ", transform=ax.transAxes,
        ha="right", va="bottom", color="w",
        family="sans-serif", fontweight="light", fontsize=16)
ax.text(0.5, 1.0, "UNCHAINED", transform=ax.transAxes,
        ha="left", va="bottom", color="w",
        family="sans-serif", fontweight="bold", fontsize=16)
```

### Step 6: Animating the Plot

We will now animate the plot by shifting the data to the right and filling in new values.

```python
def update(*args):
    # Shift all data to the right
    data[:, 1:] = data[:, :-1]

    # Fill-in new values
    data[:, 0] = np.random.uniform(0, 1, len(data))

    # Update data
    for i in range(len(data)):
        lines[i].set_ydata(i + G * data[i])

    # Return modified artists
    return lines

# Construct the animation, using the update function as the animation director.
anim = animation.FuncAnimation(fig, update, interval=10, save_count=100)
plt.show()
```

## Summary

In this lab, we learned the basics of data visualization using Matplotlib. We generated random data, created line plots, set limits and removed ticks, added a title, and animated the plot. These are just the basics, and Matplotlib provides many more options for customizing and enhancing your visualizations.
