# Python Matplotlib Lab: Text Commands

## Introduction

Matplotlib is a Python library used to create visualizations such as line plots, scatter plots, bar plots, and more. In this lab, we will learn how to use text commands to add text to our plots. We will explore different ways to add text and annotations to our plots.

## Steps

### Step 1: Importing Required Libraries

First, we need to import the `matplotlib` library and its `pyplot` module. We will use the `pyplot` module to create and customize our plots.

```python
import matplotlib.pyplot as plt
```

### Step 2: Creating a Figure and Subplot

We will create a figure and subplot using the `plt.subplots()` function. This function returns a tuple that contains a figure and a subplot. We will use the subplot to add text and annotations to our plot.

```python
fig, ax = plt.subplots()
```

### Step 3: Adding a Title to the Figure

We can add a title to the figure using the `fig.suptitle()` function. This function takes a string as an argument and sets the title of the figure.

```python
fig.suptitle('bold figure suptitle', fontsize=14, fontweight='bold')
```

### Step 4: Adding a Title to the Subplot

We can add a title to the subplot using the `ax.set_title()` function. This function takes a string as an argument and sets the title of the subplot.

```python
ax.set_title('axes title')
```

### Step 5: Adding Labels to the Axes

We can add labels to the x and y axes using the `ax.set_xlabel()` and `ax.set_ylabel()` functions, respectively. These functions take a string as an argument and set the label of the corresponding axis.

```python
ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')
```

### Step 6: Adding Text to the Plot

We can add text to the plot using the `ax.text()` function. This function takes three arguments: the x-coordinate, the y-coordinate, and the text string. We can customize the text style using the `style`, `bbox`, and `fontsize` arguments.

```python
ax.text(3, 8, 'boxed italics text in data coords', style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

ax.text(2, 6, r'an equation: $E=mc^2$', fontsize=15)

ax.text(3, 2, 'Unicode: Institut f\374r Festk\366rperphysik')

ax.text(0.95, 0.01, 'colored text in axes coords',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='green', fontsize=15)
```

### Step 7: Adding Annotations to the Plot

We can add annotations to the plot using the `ax.annotate()` function. This function takes three arguments: the annotation text, the xy-coordinate of the point to annotate, and the xy-coordinate of the text position. We can customize the annotation style using the `arrowprops` argument.

```python
ax.annotate('annotate', xy=(2, 1), xytext=(3, 4),
            arrowprops=dict(facecolor='black', shrink=0.05))
```

### Step 8: Setting the Plot Limits

We can set the x and y limits of the plot using the `ax.set()` function. This function takes two arguments: the x and y limits as tuples.

```python
ax.set(xlim=(0, 10), ylim=(0, 10))
```

### Step 9: Displaying the Plot

Finally, we can display the plot using the `plt.show()` function. This function shows the plot in a separate window.

```python
plt.show()
```

## Summary

In this lab, we learned how to use text commands to add text and annotations to our plots. We explored different ways to add text and annotations to our plots using the `ax.text()` and `ax.annotate()` functions. We also learned how to set the limits of the plot using the `ax.set()` function. By using these text commands, we can make our plots more informative and easier to understand.
