# Step-by-Step Lab: Plotting a Parametric Curve in 3D using Matplotlib

## Introduction

This lab will demonstrate how to plot a parametric curve in 3D using Matplotlib. The curve will be defined by three equations:

x = r \* sin(theta)

y = r \* cos(theta)

z = z

where r and z are defined as:

r = z^2 + 1

z is a range of values from -2 to 2, and theta is a range of values from -4π to 4π.

## Steps

### Step 1: Import necessary libraries

We will begin by importing the necessary libraries: Matplotlib and NumPy. Matplotlib will be used to create the 3D plot, and NumPy will be used to generate the values for x, y, and z.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create a 3D plot

Next, we will create a 3D plot using Matplotlib. We will also create an axis object to add labels and legends to the plot.

```python
ax = plt.figure().add_subplot(projection='3d')
```

### Step 3: Define the values for x, y, and z

We will generate the values for x, y, and z using NumPy. We will first define the range of values for theta and z. Then, we will use these values to generate the values for r, x, and y.

```python
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
```

### Step 4: Plot the parametric curve

Now that we have generated the values for x, y, and z, we can plot the parametric curve using the plot() method in Matplotlib.

```python
ax.plot(x, y, z, label='parametric curve')
```

### Step 5: Add labels and legends to the plot

Finally, we will add labels and legends to the plot using the legend() method.

```python
ax.legend()
```

### Summary

In this lab, we learned how to plot a parametric curve in 3D using Matplotlib. We defined the curve using three equations and generated the values for x, y, and z using NumPy. We then plotted the curve and added labels and legends to the plot.
