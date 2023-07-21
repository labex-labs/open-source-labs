# Arrow Plotting using Matplotlib

## Introduction

Matplotlib is a powerful plotting library in Python. It provides a variety of customizable visualizations such as line plots, scatter plots, bar graphs, histograms, and more. One of the visualizations that Matplotlib provides is the Arrow Plot. Arrow plots are used to encode arrow "strength" such as transition probabilities in a Markov model using arrow length, width, or alpha (opacity).

In this lab, we will learn how to create arrow plots using Matplotlib. We will use the `make_arrow_graph()` function to plot the arrow graph.

## Steps

### Step 1: Import Libraries and Define the Function

The first step is to import the necessary libraries and define the `make_arrow_graph()` function. This function takes in various parameters such as the axes, data, size, display, shape, max_arrow_width, arrow_sep, alpha, normalize_data, ec, labelcolor, and kwargs. It uses these parameters to create an arrow plot.

```python
# Import libraries
import itertools
import matplotlib.pyplot as plt
import numpy as np

# Define the function
def make_arrow_graph(ax, data, size=4, display='length', shape='right',
                     max_arrow_width=0.03, arrow_sep=0.02, alpha=0.5,
                     normalize_data=False, ec=None, labelcolor=None,
                     **kwargs):
    """
    Makes an arrow plot.

    Parameters
    ----------
    ax
        The axes where the graph is drawn.
    data
        Dict with probabilities for the bases and pair transitions.
    size
        Size of the plot, in inches.
    display : {'length', 'width', 'alpha'}
        The arrow property to change.
    shape : {'full', 'left', 'right'}
        For full or half arrows.
    max_arrow_width : float
        Maximum width of an arrow, in data coordinates.
    arrow_sep : float
        Separation between arrows in a pair, in data coordinates.
    alpha : float
        Maximum opacity of arrows.
    **kwargs
        `.FancyArrow` properties, e.g. *linewidth* or *edgecolor*.
    """

    # code block
```

### Step 2: Define the Data and Plot the Arrow Graph

The second step is to define the data and plot the arrow graph using the `make_arrow_graph()` function. We will define the data as a dictionary with probabilities for the bases and pair transitions. We will also set the size of the plot to 4 and normalize the data.

```python
# Define the data
data = {
    'A': 0.4, 'T': 0.3, 'G': 0.6, 'C': 0.2,
    'AT': 0.4, 'AC': 0.3, 'AG': 0.2,
    'TA': 0.2, 'TC': 0.3, 'TG': 0.4,
    'CT': 0.2, 'CG': 0.3, 'CA': 0.2,
    'GA': 0.1, 'GT': 0.4, 'GC': 0.1,
}

# Plot the arrow graph
size = 4
fig = plt.figure(figsize=(3 * size, size), layout="constrained")
axs = fig.subplot_mosaic([["length", "width", "alpha"]])

for display, ax in axs.items():
    make_arrow_graph(
        ax, data, display=display, linewidth=0.001, edgecolor=None,
        normalize_data=True, size=size)

plt.show()
```

### Step 3: Customize the Arrow Graph

The third step is to customize the arrow graph. We can change the arrow property to display using the `display` parameter. We can also change the shape of the arrow using the `shape` parameter. We can adjust the width and separation of the arrows using the `max_arrow_width` and `arrow_sep` parameters, respectively. We can change the transparency of the arrows using the `alpha` parameter. We can also change the color of the label using the `labelcolor` parameter.

```python
# Plot the arrow graph with customizations
size = 4
fig = plt.figure(figsize=(3 * size, size), layout="constrained")
axs = fig.subplot_mosaic([["length", "width", "alpha"]])

for display, ax in axs.items():
    make_arrow_graph(
        ax, data, display=display, linewidth=0.001, edgecolor=None,
        normalize_data=True, size=size, shape='full', max_arrow_width=0.05,
        arrow_sep=0.03, alpha=0.7, labelcolor='white')

plt.show()
```

### Step 4: Interpret the Arrow Graph

The fourth step is to interpret the arrow graph. The length, width, and opacity of the arrows represent the arrow strength. The arrow graph can be used to encode arrow "strength" such as transition probabilities in a Markov model using arrow length, width, or alpha (opacity). The labels on the arrows represent the probabilities for the bases and pair transitions.

## Summary

In this lab, we learned how to create arrow plots using Matplotlib. We used the `make_arrow_graph()` function to plot the arrow graph. We customized the arrow graph by changing the arrow property to display, changing the shape of the arrow, adjusting the width and separation of the arrows, changing the transparency of the arrows, and changing the color of the label. We also interpreted the arrow graph by understanding that the length, width, and opacity of the arrows represent the arrow strength, and the labels on the arrows represent the probabilities for the bases and pair transitions.
