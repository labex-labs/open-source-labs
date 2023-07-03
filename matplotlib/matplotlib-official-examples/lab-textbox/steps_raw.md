# Python Matplotlib Tutorial: Interactive Plotting with Textbox

## Introduction

In this tutorial, we will learn how to create an interactive plot with a textbox using Matplotlib. The Textbox widget allows users to provide text input, which updates the plot in real-time.

## Steps

### Step 1: Import Required Libraries

First, we need to import the necessary libraries. We will be using NumPy and Matplotlib to create the plot and the Textbox widget.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import TextBox
```

### Step 2: Create the Initial Plot

Next, we create the initial plot that will be updated based on the user's input. In this example, we create a plot of a function with `t` as the independent variable.

```python
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)

t = np.arange(-2.0, 2.0, 0.001)
l, = ax.plot(t, np.zeros_like(t), lw=2)
```

### Step 3: Define the Submit Function

We define the `submit` function that will be called when the user submits the text input. This function updates the plotted function based on the user's input.

```python
def submit(expression):
    """
    Update the plotted function to the new math *expression*.

    *expression* is a string using "t" as its independent variable, e.g.
    "t ** 3".
    """
    ydata = eval(expression, {'np': np}, {'t': t})
    l.set_ydata(ydata)
    ax.relim()
    ax.autoscale_view()
    plt.draw()
```

### Step 4: Create the Textbox Widget

We create the Textbox widget and add it to the figure. The `on_submit` method is used to trigger the `submit` function when the user presses enter in the textbox or leaves the textbox. We also set the initial value of the Textbox widget to `t ** 2`.

```python
axbox = fig.add_axes([0.1, 0.05, 0.8, 0.075])
text_box = TextBox(axbox, "Evaluate", textalignment="center")
text_box.on_submit(submit)
text_box.set_val("t ** 2")  # Trigger `submit` with the initial string.
```

### Step 5: Display the Plot

Finally, we display the plot to the user.

```python
plt.show()
```

## Summary

In this tutorial, we learned how to create an interactive plot with a textbox using Matplotlib. We created an initial plot, defined a `submit` function that updates the plot, created a Textbox widget, and displayed the plot to the user. With this knowledge, you can create your own interactive plots with user input.
