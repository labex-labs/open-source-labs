# Matplotlib Timer Tutorial

## Introduction

This lab aims to explain how to use general timer objects in Matplotlib. This is a simple example that is used to update the time placed in the title of the figure.

## Steps

### Step 1: Import Required Libraries

Import the required libraries for the code to function properly.

```python
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Define Function to Update Title

Define the function to update the title of the figure with the current time.

```python
def update_title(axes):
    axes.set_title(datetime.now())
    axes.figure.canvas.draw()
```

### Step 3: Create Figure and Axes

Create a figure and axes for the plot.

```python
fig, ax = plt.subplots()
```

### Step 4: Plot Data

Create data to plot and plot it on the axes.

```python
x = np.linspace(-3, 3)
ax.plot(x, x ** 2)
```

### Step 5: Create Timer Object

Create a new timer object. Set the interval to 100 milliseconds (1000 is default) and tell the timer what function should be called.

```python
timer = fig.canvas.new_timer(interval=100)
timer.add_callback(update_title, ax)
```

### Step 6: Start Timer

Start the timer.

```python
timer.start()
```

### Step 7: Show Plot

Show the plot.

```python
plt.show()
```

## Summary

This lab showed how to use general timer objects in Matplotlib to update the time in the title of a figure. By following the steps, users can create their own timer objects and update their plots dynamically.
