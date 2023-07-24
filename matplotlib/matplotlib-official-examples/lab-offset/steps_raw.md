# Python Matplotlib Tutorial

## Introduction

This lab will guide you through the process of creating a 3D plot using Matplotlib in Python.

## Steps

### Step 1: Import Necessary Libraries

We begin by importing the necessary libraries. In this case, we need NumPy and Matplotlib.

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
```

### Step 2: Create Data

Next, we create the data that we will use in our plot. In this example, we will be using NumPy to generate the data.

```python
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X ** 2 + Y ** 2))
```

### Step 3: Create the Figure and Axes Objects

Now, we create a figure and axes object that we will use to create the plot.

```python
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
```

### Step 4: Create the Plot

Finally, we create the plot using the data and the axes object we just created.

```python
ax.plot_surface(X, Y, Z)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
```

### Step 5: Display the Plot

We display the plot using the `plt.show()` function.

```python
plt.show()
```

## Summary

In this lab, we learned how to create a 3D plot using Matplotlib in Python. We started by importing the necessary libraries, then created the data, figure and axes objects, and finally created and displayed the plot.
