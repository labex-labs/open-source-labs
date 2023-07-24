# Python Matplotlib Tutorial Lab

## Introduction

Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy. In this tutorial, we will learn how to create a simple legend with Matplotlib.

## Steps

### Step 1: Import Matplotlib

To use Matplotlib, we need to import it first.

```python
import matplotlib.pyplot as plt
```

### Step 2: Create a Figure and Axes

We need to create a figure and axes to plot our data.

```python
fig, ax = plt.subplots()
```

### Step 3: Plot the Data

We can plot our data using the `plot()` function.

```python
line1, = ax.plot([1, 2, 3], label="Line 1", linestyle='--')
line2, = ax.plot([3, 2, 1], label="Line 2", linewidth=4)
```

### Step 4: Create the First Legend

We can create a legend for the first line using the `legend()` function.

```python
first_legend = ax.legend(handles=[line1], loc='upper right')
```

### Step 5: Add the First Legend

We need to add the first legend to the plot using the `add_artist()` function.

```python
ax.add_artist(first_legend)
```

### Step 6: Create the Second Legend

We can create another legend for the second line using the `legend()` function.

```python
ax.legend(handles=[line2], loc='lower right')
```

### Step 7: Show the Plot

We can show the plot using the `show()` function.

```python
plt.show()
```

## Summary

In this tutorial, we learned how to create a simple legend with Matplotlib. We imported Matplotlib, created a figure and axes, plotted the data, and created and added two legends to the plot. Finally, we showed the plot using the `show()` function.
