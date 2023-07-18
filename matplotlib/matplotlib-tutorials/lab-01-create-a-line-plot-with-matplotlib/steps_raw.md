# Create a Line Plot with Matplotlib

## Introduction

In this lab, we will learn how to create a line plot using Matplotlib. Line plots are a basic visualization that can be used to represent data points connected by straight line segments. We will use the Matplotlib library in Python to create a line plot.

## Steps

### Step 1: Import the necessary libraries

First, we need to import the Matplotlib library, as well as any other libraries that we will be using. In this example, we will also import the NumPy library to generate some sample data for our line plot.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Generate sample data

Next, we will generate some sample data to plot. In this example, we will create two arrays, `x` and `y`, where `x` represents the x-coordinates of the data points and `y` represents the y-coordinates.

```python
x = np.linspace(0, 10, 100)
y = np.sin(x)
```

### Step 3: Create the line plot

Now that we have our sample data, we can create the line plot using the `plot` function from the Matplotlib library. We will pass in the `x` and `y` arrays as arguments to the `plot` function.

```python
plt.plot(x, y)
```

### Step 4: Customize the plot

We can customize the plot by adding labels to the x and y axes, a title to the plot, and a legend. We can also change the line style and color.

```python
plt.plot(x, y, linestyle='--', color='red', label='sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line Plot')
plt.legend()
```

### Step 5: Display the plot

Finally, we can display the plot by calling the `show` function.

```python
plt.show()
```

## Summary

In this lab, we learned how to create a line plot using Matplotlib. We imported the necessary libraries, generated some sample data, created the line plot, customized the plot, and displayed the plot. Line plots are a useful visualization for representing data points connected by straight line segments.
