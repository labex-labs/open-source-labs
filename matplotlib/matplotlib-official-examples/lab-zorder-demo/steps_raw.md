# Matplotlib Zorder Tutorial

## Introduction

In this tutorial, we will learn about the drawing order of artists in Matplotlib and how to adjust the order using the `zorder` attribute. We will also explore how to change the order for individual artists and the default value of `zorder` for different types of artists.

## Steps

### Step 1: Understanding Zorder

The `zorder` attribute in Matplotlib is a floating point number that determines the drawing order of artists. Artists with higher `zorder` are drawn on top of those with lower `zorder`. The default value of `zorder` depends on the type of the artist. For example, images have a default `zorder` of 0, while patches have a default `zorder` of 1.

### Step 2: Changing Zorder

To change the drawing order of artists, we can set their `zorder` attribute explicitly using the `zorder` parameter when creating the artist. For example, we can move dots on top of lines in a scatter plot by setting the `zorder` of the dots to a value higher than the `zorder` of the line.

```python
import matplotlib.pyplot as plt
import numpy as np

r = np.linspace(0.3, 1, 30)
theta = np.linspace(0, 4*np.pi, 30)
x = r * np.sin(theta)
y = r * np.cos(theta)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3.2))

ax1.plot(x, y, 'C3', lw=3)
ax1.scatter(x, y, s=120)
ax1.set_title('Lines on top of dots')

ax2.plot(x, y, 'C3', lw=3)
ax2.scatter(x, y, s=120, zorder=2.5)  # move dots on top of line
ax2.set_title('Dots on top of lines')

plt.tight_layout()
plt.show()
```

### Step 3: Setting Zorder for Ticks and Grid Lines

We can use the `set_axisbelow()` method or the `axes.axisbelow` parameter to set the `zorder` of ticks and grid lines.

```python
ax = plt.axes()
ax.plot([1, 2, 3], [2, 4, 3])
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')
```

### Step 4: Custom Order of Elements

We can also set the `zorder` of elements in a custom order. For example, we can set the `zorder` of a legend to be between two lines.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 7.5, 100)
plt.rcParams['lines.linewidth'] = 5
plt.figure()
plt.plot(x, np.sin(x), label='zorder=2', zorder=2)  # bottom
plt.plot(x, np.sin(x+0.5), label='zorder=3',  zorder=3)
plt.axhline(0, label='zorder=2.5', color='lightgrey', zorder=2.5)
plt.title('Custom order of elements')
l = plt.legend(loc='upper right')
l.set_zorder(2.5)  # legend between blue and orange line
plt.show()
```

## Summary

In this tutorial, we learned about the `zorder` attribute in Matplotlib and how to change the drawing order of artists. We also explored how to set the `zorder` for ticks and grid lines and create a custom order of elements. Understanding `zorder` is essential when creating complex visualizations with overlapping elements.
