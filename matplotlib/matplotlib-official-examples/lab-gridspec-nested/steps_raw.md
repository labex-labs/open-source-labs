# Python Matplotlib Tutorial Lab

## Introduction

Matplotlib is a data visualization library in Python. It provides a wide variety of charts and graphs that can be used to represent data in various forms. In this lab, we will go through the process of creating nested gridspecs using Matplotlib.

## Steps

### Step 1: Import Matplotlib Library

The first step is to import the Matplotlib library. We will also use the `gridspec` module from Matplotlib.

```python
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
```

### Step 2: Create the Figure and Outer GridSpec

The next step is to create a figure and an outer gridspec. In this example, we will create a 1 by 2 gridspec.

```python
fig = plt.figure()
gs0 = gridspec.GridSpec(1, 2, figure=fig)
```

### Step 3: Create the Inner GridSpec

Now, we will create the inner gridspec. We will use the `GridSpecFromSubplotSpec` method to create a 3 by 3 gridspec that will be a subplot of the outer gridspec.

```python
gs00 = gridspec.GridSpecFromSubplotSpec(3, 3, subplot_spec=gs0[0])
```

### Step 4: Add Subplots to the Inner GridSpec

We will now add subplots to the inner gridspec. We will create three subplots: `ax1`, `ax2`, and `ax3`.

```python
ax1 = fig.add_subplot(gs00[:-1, :])
ax2 = fig.add_subplot(gs00[-1, :-1])
ax3 = fig.add_subplot(gs00[-1, -1])
```

### Step 5: Create Another Inner GridSpec

We will now create another inner gridspec. This time, we will use the `subgridspec` method to create a 3 by 3 gridspec that will be a subplot of the second column of the outer gridspec.

```python
gs01 = gs0[1].subgridspec(3, 3)
```

### Step 6: Add Subplots to the Second Inner GridSpec

We will now add subplots to the second inner gridspec. We will create three subplots: `ax4`, `ax5`, and `ax6`.

```python
ax4 = fig.add_subplot(gs01[:, :-1])
ax5 = fig.add_subplot(gs01[:-1, -1])
ax6 = fig.add_subplot(gs01[-1, -1])
```

### Step 7: Format the Axes

We will format the axes of all the subplots using the `format_axes` function. This function will add a text label to each subplot and remove the tick labels.

```python
def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

format_axes(fig)
```

### Step 8: Display the Figure

Finally, we will display the figure using the `show` method.

```python
plt.show()
```

## Summary

In this lab, we learned how to create nested gridspecs using Matplotlib. We created an outer gridspec and two inner gridspecs to create a complex layout of subplots. We also learned how to format the axes of the subplots using a custom function.
