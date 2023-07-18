# Python Matplotlib Tutorial - Creating a Line Plot

## Introduction

In this lab, we will learn how to create a line plot using Python Matplotlib. A line plot is a way of displaying data points on a line. It is used to show the trend of a particular set of data over time.

## Steps

### Step 1: Importing Libraries

First, we need to import the necessary libraries. We will be using the `matplotlib.pyplot` library to create our line plot.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Creating Data

Next, we need to create some data that we will plot on our line. We will use NumPy to create some random data points for our line.

```python
x = np.linspace(0, 10)
```

### Step 3: Creating the Line Plot

Now we can create our line plot using the `plot()` function from `matplotlib.pyplot`. We will plot 8 random lines using different colors from the Solarized Light color scheme.

```python
with plt.style.context('Solarize_Light2'):
    plt.plot(x, np.sin(x) + x + np.random.randn(50))
    plt.plot(x, np.sin(x) + 2 * x + np.random.randn(50))
    plt.plot(x, np.sin(x) + 3 * x + np.random.randn(50))
    plt.plot(x, np.sin(x) + 4 + np.random.randn(50))
    plt.plot(x, np.sin(x) + 5 * x + np.random.randn(50))
    plt.plot(x, np.sin(x) + 6 * x + np.random.randn(50))
    plt.plot(x, np.sin(x) + 7 * x + np.random.randn(50))
    plt.plot(x, np.sin(x) + 8 * x + np.random.randn(50))
```

### Step 4: Adding Labels and Title

We can add labels and a title to our line plot using the `xlabel()`, `ylabel()`, and `title()` functions.

```python
plt.title('8 Random Lines - Line')
plt.xlabel('x label', fontsize=14)
plt.ylabel('y label', fontsize=14)
```

### Step 5: Displaying the Plot

Finally, we can display our line plot using the `show()` function.

```python
plt.show()
```

## Summary

In this lab, we learned how to create a line plot using Python Matplotlib. We imported the necessary libraries, created some data, and used the `plot()` function to create our line plot. We added labels and a title to our plot and displayed it using the `show()` function.
