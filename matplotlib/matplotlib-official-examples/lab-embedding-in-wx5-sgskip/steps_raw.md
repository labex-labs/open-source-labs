# Step-by-Step Lab: Python Matplotlib Tutorial

## Introduction

Matplotlib is a Python library used for data visualization. It provides an interface for creating a variety of charts, plots, and graphs. In this lab, you will learn how to create a simple line plot using Matplotlib.

## Steps

### Step 1: Install Matplotlib

Before starting, you need to make sure that Matplotlib is installed. To install Matplotlib, you can use pip:

```
pip install matplotlib
```

### Step 2: Import Matplotlib

To use Matplotlib, you need to import it into your Python script:

```python
import matplotlib.pyplot as plt
```

The `plt` module is the main interface for creating plots using Matplotlib.

### Step 3: Create Data

In this step, you will create some data to use in your plot. For this tutorial, you will create two arrays, one for the x-axis and one for the y-axis:

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
```

### Step 4: Create a Figure and Axes

A figure is the overall window or page that everything is drawn on. An axes is a specific plot within the figure. In this step, you will create a figure and an axes using Matplotlib:

```python
fig, ax = plt.subplots()
```

### Step 5: Add Data to the Plot

Now that you have created the axes, you can add data to the plot. In this case, you will add the x and y data you created in Step 3:

```python
ax.plot(x, y)
```

### Step 6: Add Labels and Title to the Plot

To make the plot more informative, you can add labels to the x and y axes and a title to the plot:

```python
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_title('Title')
```

### Step 7: Save the Plot

Finally, you can save the plot to a file using the `savefig` method:

```python
plt.savefig('plot.png')
```

### Summary

In this lab, you learned how to create a simple line plot using Matplotlib. You installed Matplotlib, imported the library, created data, created a figure and axes, added data to the plot, added labels and a title to the plot, and saved the plot to a file. With this knowledge, you can create a variety of visualizations using Matplotlib.
