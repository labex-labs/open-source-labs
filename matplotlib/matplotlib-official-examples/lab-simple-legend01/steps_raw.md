# Python Matplotlib Tutorial

## Introduction

Matplotlib is a Python library that enables users to create various types of graphs and plots. This tutorial will guide you through the process of creating a legend in a Matplotlib plot.

## Steps

### Step 1: Import necessary libraries

Before we start, we need to import the necessary libraries. In this case, we will be using the Matplotlib library.

```python
import matplotlib.pyplot as plt
```

### Step 2: Create a figure and subplot

We need to create a figure and subplot to plot our data. We will be creating a plot with two subplots.

```python
fig = plt.figure()

ax = fig.add_subplot(211)
ax.plot([1, 2, 3], label="test1")
ax.plot([3, 2, 1], label="test2")

ax = fig.add_subplot(223)
ax.plot([1, 2, 3], label="test1")
ax.plot([3, 2, 1], label="test2")
```

### Step 3: Add a legend to the plot

We will now add a legend to the plot. There are two ways to add a legend in Matplotlib. We will use both methods in this example.

```python
# Method 1: Place a legend above the subplot
ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncols=2, mode="expand", borderaxespad=0.)

# Method 2: Place a legend to the right of the subplot
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
```

### Step 4: Display the plot

Finally, we will display the plot.

```python
plt.show()
```

## Summary

In this tutorial, we learned how to add a legend to a Matplotlib plot. We used two different methods to add a legend. The first method placed the legend above the subplot, while the second method placed the legend to the right of the subplot.
