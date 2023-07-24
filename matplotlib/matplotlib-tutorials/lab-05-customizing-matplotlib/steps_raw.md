# Customizing Matplotlib

## Introduction

This lab will guide you through the process of customizing Matplotlib using style sheets and `rcParams`. Matplotlib is a powerful library for creating visualizations in Python. By customizing the properties and default styles of Matplotlib, you can create unique and visually appealing plots.

## Steps

### Step 1: Setting rcParams at runtime

You can dynamically change the default runtime configuration settings in a Python script or interactively from the Python shell. The `matplotlib.rcParams` variable is global to the Matplotlib package and stores all the rc settings. To customize rcParams at runtime, you can modify it directly using the `mpl.rcParams` dictionary. Here's an example:

```python
import matplotlib as mpl

mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
```

This code changes the default line width and line style for all plots created with Matplotlib.

### Step 2: Using style sheets

Another way to change the visual appearance of plots is to set the rcParams in a style sheet and import that style sheet with `matplotlib.style.use`. A style sheet is a file that contains a set of rcParams related to the style of a plot. Matplotlib provides a number of pre-defined styles that you can use. For example, the "ggplot" style emulates the aesthetics of the ggplot library in R. You can apply a style sheet like this:

```python
import matplotlib.pyplot as plt

plt.style.use('ggplot')
```

You can also define your own custom styles and use them by calling `.style.use` with the path or URL to the style sheet.

### Step 3: Changing the matplotlibrc file

The `matplotlibrc` file is a configuration file that allows you to customize all kinds of properties in Matplotlib. It controls the defaults for properties like figure size, line width, colors, fonts, etc. You can modify the `matplotlibrc` file to customize Matplotlib according to your preferences. The file can be located in different places on your system, and Matplotlib looks for it in a specific order. Once a `matplotlibrc` file is found, it takes precedence over other settings. You can use the `matplotlib.matplotlib_fname()` function to display the path of the currently active `matplotlibrc` file.

## Summary

Matplotlib provides multiple ways to customize the properties and default styles of plots. You can set rcParams at runtime, use style sheets to change the visual appearance of plots, and modify the `matplotlibrc` file to customize Matplotlib globally. Experiment with different customizations to create unique and visually appealing plots with Matplotlib.
