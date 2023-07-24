# Step-by-Step Lab: Using Check Buttons in Python Matplotlib

## Introduction

This lab will demonstrate how to use check buttons in Python Matplotlib. Check buttons allow users to turn visual elements on and off with check buttons, similar to check boxes. We will use the `CheckButtons` function to create a plot with three different sine waves, and the ability to choose which waves are displayed with the check buttons.

## Steps

### Step 1: Import Libraries

We will start by importing the necessary libraries. We need `numpy` for generating the data and `matplotlib` for creating the plot.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import CheckButtons
```

### Step 2: Generate Data

Next, we will generate the data for our plot. We will create three sine waves with different frequencies using `numpy`.

```python
t = np.arange(0.0, 2.0, 0.01)
s0 = np.sin(2*np.pi*t)
s1 = np.sin(4*np.pi*t)
s2 = np.sin(6*np.pi*t)
```

### Step 3: Create the Plot

Now, we will create the plot using `matplotlib`. We will plot the three sine waves on the same graph and set the visibility of the first wave to `False` since we want to start with it hidden.

```python
fig, ax = plt.subplots()
l0, = ax.plot(t, s0, visible=False, lw=2, color='black', label='1 Hz')
l1, = ax.plot(t, s1, lw=2, color='red', label='2 Hz')
l2, = ax.plot(t, s2, lw=2, color='green', label='3 Hz')
fig.subplots_adjust(left=0.2)
```

### Step 4: Add Check Buttons

We will now add the check buttons to our plot using the `CheckButtons` function. We will pass the plotted lines as labels and set the initial visibility of each line. We will also adjust the properties of the check buttons to match the colors of the plotted lines.

```python
lines_by_label = {l.get_label(): l for l in [l0, l1, l2]}
line_colors = [l.get_color() for l in lines_by_label.values()]

rax = fig.add_axes([0.05, 0.4, 0.1, 0.15])
check = CheckButtons(
    ax=rax,
    labels=lines_by_label.keys(),
    actives=[l.get_visible() for l in lines_by_label.values()],
    label_props={'color': line_colors},
    frame_props={'edgecolor': line_colors},
    check_props={'facecolor': line_colors},
)
```

### Step 5: Define Callback Function

We need to define a callback function for the check buttons. This function will be called every time a check button is clicked. We will use this function to toggle the visibility of the corresponding line on the plot.

```python
def callback(label):
    ln = lines_by_label[label]
    ln.set_visible(not ln.get_visible())
    ln.figure.canvas.draw_idle()

check.on_clicked(callback)
```

### Step 6: Display the Plot

Finally, we will display the plot using the `show()` function.

```python
plt.show()
```

## Summary

In this lab, we learned how to use check buttons in Python Matplotlib. We created a plot with three different sine waves, and the ability to choose which waves are displayed with the check buttons. We used the `CheckButtons` function to create the buttons and defined a callback function to toggle the visibility of the corresponding line on the plot.
