# Matplotlib Tutorial Lab

## Introduction

This lab is designed to provide a step-by-step guide for using Matplotlib, a Python library for creating visualizations. Matplotlib is a popular data visualization tool in the scientific and engineering communities. This tutorial will walk you through the process of creating visualizations using Matplotlib.

## Steps

### Step 1: Importing Matplotlib

Before we can start creating visualizations, we need to import Matplotlib.

```python
import matplotlib.pyplot as plt
```

Here, we are importing the `pyplot` module of Matplotlib and aliasing it as `plt`. This is a common convention in the Matplotlib community.

### Step 2: Creating a Simple Plot

Now that we have imported Matplotlib, we can start creating visualizations. Let's start by creating a simple plot.

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.show()
```

Here, we are creating two lists `x` and `y` that contain the x and y values for our plot. We then use the `plot` function to create a line plot of `x` and `y`. Finally, we use the `show` function to display the plot.

### Step 3: Customizing the Plot

Now that we have a basic plot, let's customize it.

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, color='red', marker='o')
plt.title('My Plot')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.show()
```

Here, we have added some customizations to our plot. We have changed the color of the line to red and added circular markers to each data point. We have also added a title and axis labels to our plot.

### Step 4: Creating Multiple Plots

We can also create multiple plots in the same figure.

```python
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title('Plot 1')

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title('Plot 2')

plt.show()
```

Here, we are using the `subplot` function to create two plots side-by-side in the same figure. We pass three arguments to `subplot`: the number of rows, the number of columns, and the plot number. We then create a plot in each subplot.

### Step 5: Saving the Plot

Once we have created a plot, we can save it to a file.

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title('My Plot')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.savefig('my_plot.png')
```

Here, we are using the `savefig` function to save our plot to a file named `my_plot.png`.

## Summary

In this lab, we have learned how to use Matplotlib to create visualizations in Python. We started by importing Matplotlib and creating a simple plot. We then customized our plot by changing the color and adding a title and axis labels. We also learned how to create multiple plots in the same figure and how to save our plots to a file.
