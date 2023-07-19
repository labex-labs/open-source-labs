# Creating Adjacent Subplots Tutorial

## Introduction

In data visualization, it is often useful to create multiple plots that share a common axis. This can be achieved using the `subplots` function in Matplotlib. In this tutorial, we will learn how to create adjacent subplots that share a common x-axis.

## Steps

### Step 1: Import Libraries

We begin by importing the necessary libraries - `numpy` and `matplotlib.pyplot`.

```python
import numpy as np
import matplotlib.pyplot as plt
```

### Step 2: Generate Data

We generate some sample data to be plotted. Here, we use the `numpy` library to generate three arrays of data.

```python
t = np.arange(0.0, 2.0, 0.01)

s1 = np.sin(2 * np.pi * t)
s2 = np.exp(-t)
s3 = s1 * s2
```

### Step 3: Create Subplots

We create three subplots using the `subplots` function in Matplotlib. We set the `sharex` parameter to `True` to ensure that the subplots share a common x-axis. We also remove the vertical space between the subplots using the `subplots_adjust` function.

```python
fig, axs = plt.subplots(3, 1, sharex=True)
fig.subplots_adjust(hspace=0)
```

### Step 4: Plot Data

We plot the data on each subplot and set the y-tick values and limits for each plot.

```python
axs[0].plot(t, s1)
axs[0].set_yticks(np.arange(-0.9, 1.0, 0.4))
axs[0].set_ylim(-1, 1)

axs[1].plot(t, s2)
axs[1].set_yticks(np.arange(0.1, 1.0, 0.2))
axs[1].set_ylim(0, 1)

axs[2].plot(t, s3)
axs[2].set_yticks(np.arange(-0.9, 1.0, 0.4))
axs[2].set_ylim(-1, 1)
```

### Step 5: Display Plot

We display the plot using the `show` function in Matplotlib.

```python
plt.show()
```

## Summary

In this tutorial, we learned how to create adjacent subplots that share a common x-axis using the `subplots` function in Matplotlib. We also learned how to set the y-tick values and limits for each plot. This technique is useful in data visualization to compare multiple datasets that share a common axis.
