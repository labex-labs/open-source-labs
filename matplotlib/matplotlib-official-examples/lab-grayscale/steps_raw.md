# Matplotlib Grayscale Style Sheet Lab

## Introduction

Matplotlib is a data visualization library in Python used to create a variety of charts, graphs, and plots. It provides a wide range of customization options to create attractive visualizations. One of these options is style sheets. A style sheet is a collection of settings that define the look of a plot. In this lab, we will explore the "grayscale" style sheet, which changes all colors to grayscale.

## Steps

### Step 1: Importing the Required Libraries

We start by importing the required libraries. We will need NumPy and Matplotlib.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Setting Up the Random State

To ensure the reproducibility of the results, we set up the random state using the following code:

```python
np.random.seed(19680801)
```

### Step 3: Defining the Color Cycle Example Function

We define the `color_cycle_example` function that takes an axis object as input and plots a sine wave for each color in the color cycle. The color cycle is defined by the rcParams.

```python
def color_cycle_example(ax):
    L = 6
    x = np.linspace(0, L)
    ncolors = len(plt.rcParams['axes.prop_cycle'])
    shift = np.linspace(0, L, ncolors, endpoint=False)
    for s in shift:
        ax.plot(x, np.sin(x + s), 'o-')
```

### Step 4: Defining the Image and Patch Example Function

We define the `image_and_patch_example` function that takes an axis object as input, plots a random image, and adds a patch to the plot.

```python
def image_and_patch_example(ax):
    ax.imshow(np.random.random(size=(20, 20)), interpolation='none')
    c = plt.Circle((5, 5), radius=5, label='patch')
    ax.add_patch(c)
```

### Step 5: Using the Grayscale Style Sheet

We set the style sheet to "grayscale" using the following code:

```python
plt.style.use('grayscale')
```

### Step 6: Creating the Subplots

We create a figure with two subplots using the following code:

```python
fig, (ax1, ax2) = plt.subplots(ncols=2)
fig.suptitle("'grayscale' style sheet")
```

### Step 7: Plotting the Examples

We plot the color cycle example on the first subplot and the image and patch example on the second subplot using the following code:

```python
color_cycle_example(ax1)
image_and_patch_example(ax2)
```

### Step 8: Displaying the Plot

We display the plot using the following code:

```python
plt.show()
```

## Summary

In this lab, we learned how to use the "grayscale" style sheet in Matplotlib to create plots with all colors in grayscale. We also learned how to create subplots, plot examples, and display the plot. Style sheets are an excellent way to customize the look of your plots, and Matplotlib provides many built-in style sheets to choose from.
