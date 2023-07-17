# Python Matplotlib Tutorial - Creating a Color Demo Chart

## Introduction

In this lab, we will learn how to create a color demo chart using Python's Matplotlib library. Matplotlib provides a variety of ways to specify colors, which can be used in charts, graphs, and other visualizations. We will explore these different ways of specifying colors and use them to create a chart showing voltage vs. time.

## Steps

### Step 1: Import Required Libraries

Before we begin, we need to import the Matplotlib and NumPy libraries:

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Define Data

Next, we need to define the data that we will use for our chart. We will create a sine wave with 201 data points:

```python
t = np.linspace(0.0, 2.0, 201)
s = np.sin(2 * np.pi * t)
```

### Step 3: Specify Colors

Matplotlib provides several ways to specify colors, including:

1. An RGB or RGBA tuple of float values in [0, 1].
2. A hex RGB or RGBA string.
3. A shorthand hex RGB or RGBA string.
4. A string representation of a float value in [0, 1] inclusive for gray level.
5. A single letter string, i.e. one of {'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'}.
6. A X11/CSS4 ("html") color name.
7. A name from the xkcd color survey, prefixed with 'xkcd:'.
8. A "Cn" color spec, i.e. 'C' followed by a number.
9. One of {'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'}.

We will use several of these methods to specify the colors for our chart.

### Step 4: Create Chart

Now we can create our chart using the data and colors that we have specified:

```python
fig, ax = plt.subplots(facecolor=(.18, .31, .31))
ax.set_facecolor('#eafff5')
ax.set_title('Voltage vs. time chart', color='0.7')
ax.set_xlabel('Time [s]', color='c')
ax.set_ylabel('Voltage [mV]', color='peachpuff')
ax.plot(t, s, 'xkcd:crimson')
ax.plot(t, .7*s, color='C4', linestyle='--')
ax.tick_params(labelcolor='tab:orange')
```

### Step 5: Display Chart

Finally, we can display our chart using the following command:

```python
plt.show()
```

## Summary

In this lab, we learned how to create a color demo chart using Python's Matplotlib library. We explored several ways to specify colors and used them to create a chart showing voltage vs. time. We hope that this tutorial has been helpful in learning how to use Matplotlib to create charts and visualizations.
