# Python Matplotlib Tutorial

## Introduction

In this lab, you will learn how to use Matplotlib, a Python library for creating visualizations, to create a figure and annotate its anatomy. You will learn how to create a figure, plot data, set axis limits, add labels and titles, and annotate the figure with text and markers.

## Steps

### Step 1: Import libraries and set up data

First, we need to import the necessary libraries and set up some data to plot. In this example, we will plot three sine waves with some random noise added to them.

```python
import matplotlib.pyplot as plt
import numpy as np

# Set up data
np.random.seed(19680801)

X = np.linspace(0.5, 3.5, 100)
Y1 = 3+np.cos(X)
Y2 = 1+np.cos(1+X/0.75)/2
Y3 = np.random.uniform(Y1, Y2, len(X))
```

### Step 2: Create the figure and set up the axes

Next, we will create a figure and set up the axes. We will use the `add_axes()` method to create a new set of axes within the figure. We will also set limits for the x and y axes and add gridlines.

```python
# Create figure and axes
fig = plt.figure(figsize=(7.5, 7.5))
ax = fig.add_axes([0.2, 0.17, 0.68, 0.7], aspect=1)

# Set limits and gridlines
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)
```

### Step 3: Plot the data

Now we will plot our data on the axes we just created. We will use the `plot()` method to plot the three sine waves with different colors and line widths.

```python
# Plot data
ax.plot(X, Y1, c='C0', lw=2.5, label="Blue signal", zorder=10)
ax.plot(X, Y2, c='C1', lw=2.5, label="Orange signal")
ax.plot(X[::3], Y3[::3], linewidth=0, markersize=9,
        marker='s', markerfacecolor='none', markeredgecolor='C4',
        markeredgewidth=2.5)
```

### Step 4: Add labels and title

We will now add labels to the x and y axes, and a title to the figure using the `set_xlabel()`, `set_ylabel()`, and `set_title()` methods.

```python
# Add labels and title
ax.set_xlabel("x Axis label", fontsize=14)
ax.set_ylabel("y Axis label", fontsize=14)
ax.set_title("Anatomy of a figure", fontsize=20, verticalalignment='bottom')
```

### Step 5: Add legend

We will add a legend to the figure using the `legend()` method. We will also specify the location and font size of the legend.

```python
# Add legend
ax.legend(loc="upper right", fontsize=14)
```

### Step 6: Annotate the figure

Finally, we will annotate the figure to show the names of various Matplotlib elements using the `text()` and `Circle()` methods. We will also use the `withStroke()` method to add a white outline to the text and markers for better visibility.

```python
# Annotate the figure
from matplotlib.patches import Circle
from matplotlib.patheffects import withStroke

royal_blue = [0, 20/256, 82/256]

def annotate(x, y, text, code):
    # Circle marker
    c = Circle((x, y), radius=0.15, clip_on=False, zorder=10, linewidth=2.5,
               edgecolor=royal_blue + [0.6], facecolor='none',
               path_effects=[withStroke(linewidth=7, foreground='white')])
    ax.add_artist(c)

    # use path_effects as a background for the texts
    # draw the path_effects and the colored text separately so that the
    # path_effects cannot clip other texts
    for path_effects in [[withStroke(linewidth=7, foreground='white')], []]:
        color = 'white' if path_effects else royal_blue
        ax.text(x, y-0.2, text, zorder=100,
                ha='center', va='top', weight='bold', color=color,
                style='italic', fontfamily='Courier New',
                path_effects=path_effects)

        color = 'white' if path_effects else 'black'
        ax.text(x, y-0.33, code, zorder=100,
                ha='center', va='top', weight='normal', color=color,
                fontfamily='monospace', fontsize='medium',
                path_effects=path_effects)

annotate(3.5, -0.13, "Minor tick label", "ax.xaxis.set_minor_formatter")
annotate(-0.03, 1.0, "Major tick", "ax.yaxis.set_major_locator")
annotate(0.00, 3.75, "Minor tick", "ax.yaxis.set_minor_locator")
annotate(-0.15, 3.00, "Major tick label", "ax.yaxis.set_major_formatter")
annotate(1.68, -0.39, "xlabel", "ax.set_xlabel")
annotate(-0.38, 1.67, "ylabel", "ax.set_ylabel")
annotate(1.52, 4.15, "Title", "ax.set_title")
annotate(1.75, 2.80, "Line", "ax.plot")
annotate(2.25, 1.54, "Markers", "ax.scatter")
annotate(3.00, 3.00, "Grid", "ax.grid")
annotate(3.60, 3.58, "Legend", "ax.legend")
annotate(2.5, 0.55, "Axes", "fig.subplots")
annotate(4, 4.5, "Figure", "plt.figure")
annotate(0.65, 0.01, "x Axis", "ax.xaxis")
annotate(0, 0.36, "y Axis", "ax.yaxis")
annotate(4.0, 0.7, "Spine", "ax.spines")
```

### Summary

In this lab, you learned how to use Matplotlib to create a figure and annotate its anatomy. You learned how to create a figure, plot data, set axis limits, add labels and titles, and annotate the figure with text and markers. By following the steps in this lab, you should now have a good understanding of how to use Matplotlib to create and annotate figures in Python.
