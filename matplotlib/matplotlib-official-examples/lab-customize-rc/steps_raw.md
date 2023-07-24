# Matplotlib Tutorial Lab

## Introduction

This lab will guide you through the process of customizing `.rcParams` on the fly using Python Matplotlib. You will learn how to define functions in a custom module that set the defaults for figures, and how to use these defaults to create different sets of defaults for figures, such as one set for publication and another set for interactive exploration.

## Steps

### Step 1: Create a Function to Set Default Parameters

To create a function that sets the default parameters for your figures, you can use the `rcParams.update()` method. This method takes a dictionary of parameter names and values, and updates the current default values with the new ones. Here's an example of a function that sets some default parameters for publication figures:

```python
def set_pub():
    rcParams.update({
        "font.weight": "bold",  # bold fonts
        "tick.labelsize": 15,   # large tick labels
        "lines.linewidth": 1,   # thick lines
        "lines.color": "k",     # black lines
        "grid.color": "0.5",    # gray gridlines
        "grid.linestyle": "-",  # solid gridlines
        "grid.linewidth": 0.5,  # thin gridlines
        "savefig.dpi": 300,     # higher resolution output.
    })
```

### Step 2: Customize Default Parameters

To customize the default parameters for a specific figure, you can use the `rcParams.update()` method again. This time, you'll pass a dictionary of parameter names and values that you want to set for that figure. Here's an example that sets some default parameters for a specific figure:

```python
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.weight": "bold",
    "xtick.major.size": 5,
    "xtick.major.pad": 7,
    "xtick.labelsize": 15,
    "grid.color": "0.5",
    "grid.linestyle": "-",
    "grid.linewidth": 5,
    "lines.linewidth": 2,
    "lines.color": "g",
})
```

### Step 3: Create Subplots

To create subplots in Matplotlib, you can use the `subplot()` method. This method takes three arguments: the number of rows, the number of columns, and the plot number. Here's an example that creates three subplots:

```python
plt.subplot(311)
plt.plot([1, 2, 3])

plt.subplot(312)
plt.plot([1, 2, 3])
plt.grid(True)

plt.subplot(313)
plt.plot([1, 2, 3])
plt.grid(True)
```

### Step 4: Show the Figure

To show the figure, you can use the `show()` method. Here's an example:

```python
plt.show()
```

### Step 5: Reset Default Parameters

To reset the default parameters to their original values, you can use the `rcdefaults()` method. Here's an example:

```python
plt.rcdefaults()
```

## Summary

In this lab, you learned how to customize `.rcParams` on the fly using Python Matplotlib. You learned how to define functions that set the default parameters for your figures, how to customize the default parameters for a specific figure, how to create subplots, how to show the figure, and how to reset the default parameters to their original values. With these skills, you can create customized figures for your publications and interactive explorations.
