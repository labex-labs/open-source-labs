# Creating 2D Bar Graphs in Different Planes

## Introduction

In this lab, we will learn how to create a 3D plot with 2D bar graphs projected onto different planes. We will use the Matplotlib library in Python to generate the visualizations. This lab assumes a basic understanding of Python syntax and the Matplotlib library.

## Steps

### Step 1: Import Libraries

We will begin by importing the necessary libraries for this lab. We will use the NumPy library to generate random data and the Matplotlib library to create the 3D plot.

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
```

### Step 2: Create a Figure and Subplot

Next, we will create a figure and subplot for our 3D plot. We will use the `add_subplot()` method to create a 3D projection.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
```

### Step 3: Generate Data for the Bar Graphs

We will now generate the data for the bar graphs. We will create four sets of data, each with 20 values. We will use the NumPy `arange()` method to create an array of 20 values and the NumPy `random.rand()` method to generate random values for each set of data.

```python
colors = ['r', 'g', 'b', 'y']
yticks = [3, 2, 1, 0]
for c, k in zip(colors, yticks):
    xs = np.arange(20)
    ys = np.random.rand(20)
```

### Step 4: Customize the Bar Graphs

We will now customize the bar graphs. We will create an array of colors and use the `bar()` method to plot the bar graphs. We will set the `zdir` parameter to 'y' to project the bar graphs onto the y-axis planes. We will also set the `alpha` parameter to 0.8 to adjust the transparency of the bars.

```python
    cs = [c] * len(xs)
    cs[0] = 'c'
    ax.bar(xs, ys, zs=k, zdir='y', color=cs, alpha=0.8)
```

### Step 5: Customize the Axes

We will now customize the axes of the 3D plot. We will set the labels for the x, y, and z axes using the `set_xlabel()`, `set_ylabel()`, and `set_zlabel()` methods, respectively. We will also set the ticks on the y-axis using the `set_yticks()` method.

```python
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_yticks(yticks)
```

### Step 6: Display the Plot

We will use the `show()` method to display the 3D plot.

```python
plt.show()
```

## Summary

In this lab, we learned how to create a 3D plot with 2D bar graphs projected onto different planes using the Matplotlib library in Python. We generated random data and customized the bar graphs and axes of the plot. We then displayed the plot using the `show()` method.
