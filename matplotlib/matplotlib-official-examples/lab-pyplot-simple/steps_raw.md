# Python Matplotlib Tutorial

## Introduction

Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK. It also provides a procedural interface for non-interactive plotting.

In this lab, you will learn how to create a simple plot using Matplotlib.

## Steps

### Step 1: Import the Matplotlib Library

To use Matplotlib in Python, you need to import it first. Type the following code to import the Matplotlib library:

```python
import matplotlib.pyplot as plt
```

### Step 2: Create a Simple Plot

To create a simple plot in Matplotlib, you need to provide a list of numbers that you want to plot. In this case, we will plot a list of numbers against their index resulting in a straight line. Use a format string (here, 'o-r') to set the markers (circles), linestyle (solid line) and color (red).

```python
plt.plot([1, 2, 3, 4], 'o-r')
plt.ylabel('some numbers')
plt.show()
```

### Step 3: Customize the Plot

Matplotlib provides many options to customize the plot. You can change the color, linestyle, marker style, and many other options. Here is an example of how to change the color of the line to blue and the marker style to a plus sign:

```python
plt.plot([1, 2, 3, 4], '+-b')
plt.ylabel('some numbers')
plt.show()
```

### Step 4: Add Labels and Titles

Adding labels and titles to the plot is essential to make it more informative. The following code adds a title to the plot and labels to the x and y-axis:

```python
plt.plot([1, 2, 3, 4], 'o-r')
plt.title('Simple Plot')
plt.xlabel('Index')
plt.ylabel('Numbers')
plt.show()
```

### Step 5: Save the Plot

You can save the plot as an image file using the `savefig` method. The following code saves the plot as a PNG image:

```python
plt.plot([1, 2, 3, 4], 'o-r')
plt.title('Simple Plot')
plt.xlabel('Index')
plt.ylabel('Numbers')
plt.savefig('simple_plot.png')
```

## Summary

In this lab, you have learned how to create a simple plot using Matplotlib. You have also learned how to customize the plot, add labels and titles, and save the plot as an image file. Matplotlib provides many options to create informative and visually appealing plots.
