# Matplotlib Subfigures Lab

## Introduction

Matplotlib is a Python library used for creating visualizations, such as graphs, charts, and figures. In this lab, you will learn how to create subfigures in Matplotlib. Subfigures are figures that contain two or more plots within the same figure. Subfigures can help you to compare different data sets or to show different views of the same data. They are useful when you want to display multiple plots together.

## Steps

### Step 1: Import Libraries

To use Matplotlib, you need to import it. You will also need to import NumPy to create arrays for the plots.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Create a Figure with Subfigures

To create a figure with subfigures, you first need to create a figure object using `plt.figure()`. Then, you can create subfigures using `fig.subfigures()`.

```python
fig = plt.figure()
subfigs = fig.subfigures(2, 1)
```

This will create a figure with two subfigures, one above the other.

### Step 3: Plot Data on Subfigures

To plot data on the subfigures, you need to create a subplot for each subfigure using `subfig.subplots()`. Then, you can use any of the plotting functions in Matplotlib to create the plots.

```python
ax1 = subfigs[0].subplots()
ax1.plot(np.arange(10), np.random.randn(10))

ax2 = subfigs[1].subplots()
ax2.plot(np.arange(10), np.random.randn(10))
```

This will create two subfigures, each with a plot of random data.

### Step 4: Customize Subfigures

You can customize the subfigures using the various functions available in Matplotlib. For example, you can set the title and axis labels using `set_title()` and `set_xlabel()`/`set_ylabel()`.

```python
ax1.set_title('Subfigure 1')
ax1.set_xlabel('X Label')
ax1.set_ylabel('Y Label')

ax2.set_title('Subfigure 2')
ax2.set_xlabel('X Label')
ax2.set_ylabel('Y Label')
```

This will set the titles and axis labels for each subfigure.

### Step 5: Display the Figure

To display the figure, you need to use `plt.show()`.

```python
plt.show()
```

This will display the figure with the two subfigures.

## Summary

In this lab, you learned how to create subfigures in Matplotlib. You learned how to create a figure with subfigures, plot data on the subfigures, customize the subfigures, and display the figure. Subfigures can be useful when you want to compare different data sets or to show different views of the same data.
