# Legend Picking Lab

## Introduction

In this lab, we will learn how to enable picking on the legend to toggle the original line on and off using Python Matplotlib.

## Steps

### Step 1: Import Required Libraries

First, we need to import the required libraries, which are NumPy and Matplotlib.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Prepare Data

We will generate two sine waves with different frequencies using NumPy.

```python
t = np.linspace(0, 1)
y1 = 2 * np.sin(2*np.pi*t)
y2 = 4 * np.sin(2*np.pi*2*t)
```

### Step 3: Create Figure and Axes

We will create a figure and axes using Matplotlib and set the title of the plot.

```python
fig, ax = plt.subplots()
ax.set_title('Click on legend line to toggle line on/off')
```

### Step 4: Create Lines and Legend

We will create two lines and a legend using Matplotlib.

```python
line1, = ax.plot(t, y1, lw=2, label='1 Hz')
line2, = ax.plot(t, y2, lw=2, label='2 Hz')
leg = ax.legend(fancybox=True, shadow=True)
```

### Step 5: Map Legend Lines to Original Lines

We will map the legend lines to the original lines using a dictionary.

```python
lines = [line1, line2]
lined = {}  # Will map legend lines to original lines.
for legline, origline in zip(leg.get_lines(), lines):
    legline.set_picker(True)  # Enable picking on the legend line.
    lined[legline] = origline
```

### Step 6: Define the On Pick Event Function

We will define the on pick event function that will toggle the visibility of the original line corresponding to the legend proxy line.

```python
def on_pick(event):
    # On the pick event, find the original line corresponding to the legend
    # proxy line, and toggle its visibility.
    legline = event.artist
    origline = lined[legline]
    visible = not origline.get_visible()
    origline.set_visible(visible)
    # Change the alpha on the line in the legend, so we can see what lines
    # have been toggled.
    legline.set_alpha(1.0 if visible else 0.2)
    fig.canvas.draw()
```

### Step 7: Connect the On Pick Event Function to the Canvas

We will connect the on pick event function to the canvas.

```python
fig.canvas.mpl_connect('pick_event', on_pick)
```

### Step 8: Show the Plot

We will show the plot using Matplotlib.

```python
plt.show()
```

## Summary

In this lab, we learned how to enable picking on the legend to toggle the original line on and off using Python Matplotlib. We created a figure and axes, prepared data, created lines and legend, mapped legend lines to original lines, defined the on pick event function, connected the on pick event function to the canvas, and showed the plot.
