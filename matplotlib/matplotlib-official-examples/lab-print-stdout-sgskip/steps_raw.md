# AI Assistant: Python Matplotlib Tutorial

## Introduction

Matplotlib is a Python library used for plotting graphs and data visualizations. In this lab, you will learn how to use Matplotlib to create and save a simple line plot.

## Steps

### Step 1: Import necessary libraries

To use Matplotlib, we first need to import it along with other necessary libraries. The code for this is shown below:

```python
import matplotlib.pyplot as plt
```

### Step 2: Create a dataset

Next, we need to create a dataset to plot. In this example, we will use a simple list of numbers. The code for this is shown below:

```python
data = [1, 2, 3, 4, 5]
```

### Step 3: Create a plot

Now that we have our data, we can create a plot. In this example, we will create a simple line plot using the `plot()` function. The code for this is shown below:

```python
plt.plot(data)
```

### Step 4: Customize the plot

We can customize the plot by adding a title, labels for the x-axis and y-axis, and a grid. The code for this is shown below:

```python
plt.title("My Plot")
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.grid(True)
```

### Step 5: Save the plot

Finally, we can save the plot to a file using the `savefig()` function. In this example, we will save the plot as a PNG file. The code for this is shown below:

```python
plt.savefig("my_plot.png")
```

## Summary

In this lab, you learned how to use Matplotlib to create a simple line plot and save it as a PNG file. You also learned how to customize the plot by adding a title, labels for the x-axis and y-axis, and a grid. Matplotlib is a powerful library that can be used for many types of data visualizations and can help you gain insights into your data.
