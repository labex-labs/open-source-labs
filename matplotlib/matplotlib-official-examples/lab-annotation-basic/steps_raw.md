# Annotating a Plot using Matplotlib

## Introduction

This tutorial will guide you through the process of annotating a plot using Matplotlib. Annotating a plot is a useful way to highlight specific features or data points on a graph. In this tutorial, we will demonstrate how to annotate a plot with an arrow pointing to provided coordinates.

## Steps

### Step 1: Import Libraries

Before we begin, we need to import the necessary libraries. In this tutorial, we will be using Matplotlib and Numpy.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create a Plot

Next, we will create a plot using Matplotlib. In this example, we will plot the cosine function over a range of values.

```python
fig, ax = plt.subplots()

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = ax.plot(t, s, lw=2)
```

### Step 3: Annotate the Plot

Now, we will annotate the plot by adding an arrow pointing to a specific coordinate. In this example, we will add an arrow pointing to the local maximum of the cosine function.

```python
ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
```

The `ax.annotate()` function takes several arguments. The first argument is the text that will be displayed on the plot. The `xy` argument specifies the coordinates of the point that we want to annotate. The `xytext` argument specifies the coordinates of the text. The `arrowprops` argument is a dictionary that specifies the properties of the arrow.

### Step 4: Set the Plot Limits

Finally, we will set the limits of the plot to ensure that the annotated point is visible.

```python
ax.set_ylim(-2, 2)
plt.show()
```

## Summary

In this tutorial, we have learned how to annotate a plot using Matplotlib. We started by importing the necessary libraries and creating a plot. Then, we annotated the plot by adding an arrow pointing to a specific coordinate. Finally, we set the limits of the plot to ensure that the annotated point is visible.
