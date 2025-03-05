# Basic Plotting with Default Title Position

In this step, you will create a simple line plot and add a centered title, which is the default position in Matplotlib.

## Creating a Jupyter Notebook

First, let's create a new notebook:

1. In the Jupyter interface that has opened, click the "New" button at the top right and select "Python 3" to create a new notebook.
2. Rename your notebook by clicking on "Untitled" at the top of the page and entering "titles-demo".

## Importing Matplotlib

Now, let's start by importing the Matplotlib library. In the first cell of your notebook, type the following code and run it by pressing Shift+Enter:

```python
import matplotlib.pyplot as plt
```

This imports the pyplot module from Matplotlib and assigns it the alias `plt`, which is a common convention.

## Creating a Simple Plot

Next, let's create a basic line plot. In a new cell, enter the following code and run it:

```python
plt.figure(figsize=(8, 5))  # Create a figure with a specific size
plt.plot(range(10))         # Plot numbers from 0 to 9
plt.grid(True)              # Add a grid for better readability
plt.show()                  # Display the plot
```

You should see a simple line plot with values from 0 to 9 displayed in the output.

## Adding a Default (Centered) Title

Now, let's add a title to our plot. The default position for a title is centered along the top of the plot. In a new cell, enter the following code:

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('My First Matplotlib Plot')  # Add a centered title
plt.show()
```

Run the cell, and you should see the plot with a centered title at the top.

The `title()` function without any additional parameters will place the title in the center, which is the default position.
