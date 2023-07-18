# Matplotlib Axis Direction Lab

## Introduction

Matplotlib is a popular data visualization library in Python. It provides a wide variety of options for customizing plots and charts. In this lab, we will explore how to set the axis direction in Matplotlib using the `mpl_toolkits.axisartist` module.

## Steps

### Step 1: Import Libraries

Before we begin, we need to import the necessary libraries. In this lab, we will be using `matplotlib.pyplot` and `mpl_toolkits.axisartist`.

```python
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
```

### Step 2: Create a Function to Set Up Axes

We will create a function called `setup_axes` to set up the axes for our plots. This function takes in two parameters, a `fig` object and a `pos` object. The `fig` object is the figure object that we will be plotting on, and the `pos` object is the position of the subplot within the figure.

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axisartist.Axes)

    ax.set_ylim(-0.1, 1.5)
    ax.set_yticks([0, 1])

    ax.axis[:].set_visible(False)

    ax.axis["x"] = ax.new_floating_axis(1, 0.5)
    ax.axis["x"].set_axisline_style("->", size=1.5)

    return ax
```

### Step 3: Set Up Axis Direction

We will now create a figure object and set up the axis direction for our plots. We will create five different subplots to demonstrate different axis directions.

```python
plt.rcParams.update({
    "axes.titlesize": "medium",
    "axes.titley": 1.1,
})

fig = plt.figure(figsize=(10, 4))
fig.subplots_adjust(bottom=0.1, top=0.9, left=0.05, right=0.95)

ax1 = setup_axes(fig, 251)
ax1.axis["x"].set_axis_direction("left")

ax2 = setup_axes(fig, 252)
ax2.axis["x"].label.set_text("Label")
ax2.axis["x"].toggle(ticklabels=False)
ax2.axis["x"].set_axislabel_direction("+")
ax2.set_title("label direction=$+$")

ax3 = setup_axes(fig, 253)
ax3.axis["x"].label.set_text("Label")
ax3.axis["x"].toggle(ticklabels=False)
ax3.axis["x"].set_axislabel_direction("-")
ax3.set_title("label direction=$-$")

ax4 = setup_axes(fig, 254)
ax4.axis["x"].set_ticklabel_direction("+")
ax4.set_title("ticklabel direction=$+$")

ax5 = setup_axes(fig, 255)
ax5.axis["x"].set_ticklabel_direction("-")
ax5.set_title("ticklabel direction=$-$")

ax7 = setup_axes(fig, 257)
ax7.axis["x"].label.set_text("rotation=10")
ax7.axis["x"].label.set_rotation(10)
ax7.axis["x"].toggle(ticklabels=False)

ax8 = setup_axes(fig, 258)
ax8.axis["x"].set_axislabel_direction("-")
ax8.axis["x"].label.set_text("rotation=10")
ax8.axis["x"].label.set_rotation(10)
ax8.axis["x"].toggle(ticklabels=False)

plt.show()
```

### Step 4: Interpretation of Results

The code will produce a figure with five subplots that demonstrate different axis directions. The following is a summary of the subplots:

1. Subplot 1: The axis direction is set to left.
2. Subplot 2: The axis label direction is set to positive.
3. Subplot 3: The axis label direction is set to negative.
4. Subplot 4: The tick label direction is set to positive.
5. Subplot 5: The tick label direction is set to negative.

## Summary

In this lab, we learned how to set the axis direction in Matplotlib using the `mpl_toolkits.axisartist` module. We created a function to set up the axes for our plots and demonstrated different axis directions using multiple subplots. This is a useful tool for customizing plots and charts in Matplotlib.
