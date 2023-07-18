# Matplotlib Line Styles Lab

## Introduction

Matplotlib is a powerful data visualization tool for Python. One of its features is the ability to create custom line styles for plots. In this lab, we will learn how to create and use different line styles in Matplotlib.

## Steps

### Step 1: Import the required libraries

To use Matplotlib, we first need to import the library. We will also import the NumPy library to generate some sample data for our plots.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Step 2: Define line styles

There are different ways to define line styles in Matplotlib. We can use predefined styles such as 'solid', 'dashed', 'dotted', and 'dashdot'. We can also define custom line styles using a dash tuple.

```python
linestyle_str = [
     ('solid', 'solid'),      # Same as (0, ()) or '-'
     ('dotted', 'dotted'),    # Same as (0, (1, 1)) or ':'
     ('dashed', 'dashed'),    # Same as '--'
     ('dashdot', 'dashdot')]  # Same as '-.'

linestyle_tuple = [
     ('loosely dotted',        (0, (1, 10))),
     ('dotted',                (0, (1, 1))),
     ('densely dotted',        (0, (1, 1))),
     ('long dash with offset', (5, (10, 3))),
     ('loosely dashed',        (0, (5, 10))),
     ('dashed',                (0, (5, 5))),
     ('densely dashed',        (0, (5, 1))),

     ('loosely dashdotted',    (0, (3, 10, 1, 10))),
     ('dashdotted',            (0, (3, 5, 1, 5))),
     ('densely dashdotted',    (0, (3, 1, 1, 1))),

     ('dashdotdotted',         (0, (3, 5, 1, 5, 1, 5))),
     ('loosely dashdotdotted', (0, (3, 10, 1, 10, 1, 10))),
     ('densely dashdotdotted', (0, (3, 1, 1, 1, 1, 1)))]
```

### Step 3: Create a function to plot line styles

We can create a function to plot the different line styles. The function takes an axis object, a list of line styles, and a title as input parameters.

```python
def plot_linestyles(ax, linestyles, title):
    X, Y = np.linspace(0, 100, 10), np.zeros(10)
    yticklabels = []

    for i, (name, linestyle) in enumerate(linestyles):
        ax.plot(X, Y+i, linestyle=linestyle, linewidth=1.5, color='black')
        yticklabels.append(name)

    ax.set_title(title)
    ax.set(ylim=(-0.5, len(linestyles)-0.5),
           yticks=np.arange(len(linestyles)),
           yticklabels=yticklabels)
    ax.tick_params(left=False, bottom=False, labelbottom=False)
    ax.spines[:].set_visible(False)

    for i, (name, linestyle) in enumerate(linestyles):
        ax.annotate(repr(linestyle),
                    xy=(0.0, i), xycoords=ax.get_yaxis_transform(),
                    xytext=(-6, -12), textcoords='offset points',
                    color="blue", fontsize=8, ha="right", family="monospace")
```

### Step 4: Create the plot

We can create the plot by calling the `plot_linestyles` function for each set of line styles.

```python
fig, (ax0, ax1) = plt.subplots(2, 1, figsize=(10, 8), height_ratios=[1, 3])

plot_linestyles(ax0, linestyle_str[::-1], title='Named linestyles')
plot_linestyles(ax1, linestyle_tuple[::-1], title='Parametrized linestyles')

plt.tight_layout()
plt.show()
```

### Step 5: Interpret the plot

The resulting plot shows the different line styles. The top plot shows named line styles while the bottom plot shows parametrized line styles. The annotations on the right side show the dash tuples used for each line style.

## Summary

In this lab, we learned how to create and use different line styles in Matplotlib. We defined line styles using predefined styles and dash tuples. We also created a function to plot the different line styles and interpreted the resulting plot.
