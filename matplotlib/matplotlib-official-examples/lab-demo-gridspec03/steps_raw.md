# Matplotlib GridSpec Tutorial

## Introduction

In this tutorial, we will learn how to use `GridSpec` to generate subplots, control the relative sizes of subplots with _width_ratios_ and _height_ratios_, and the spacing around and between subplots using subplot params (_left_, _right_, _bottom_, _top_, _wspace_, and _hspace_).

## Steps

### Step 1: Import Libraries

We start by importing the necessary libraries, which are `matplotlib.pyplot` and `GridSpec`.

```python
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
```

### Step 2: Generate Subplots with `GridSpec`

In this step, we will use `GridSpec` to generate subplots. We will create a figure with 2 rows and 2 columns. We will also specify the `width_ratios` and `height_ratios` to control the relative sizes of the subplots.

```python
fig = plt.figure()
gs = GridSpec(2, 2, width_ratios=[1, 2], height_ratios=[4, 1])
ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])
ax3 = fig.add_subplot(gs[2])
ax4 = fig.add_subplot(gs[3])
```

### Step 3: Control Spacing Around and Between Subplots

In this step, we will use `GridSpec` to control the spacing around and between subplots. We will create a figure with 2 gridspecs, each with 3 rows and 3 columns. We will specify the `left`, `right`, `bottom`, `top`, `wspace`, and `hspace` parameters to control the spacing.

```python
fig = plt.figure()
gs1 = GridSpec(3, 3, left=0.05, right=0.48, wspace=0.05)
ax1 = fig.add_subplot(gs1[:-1, :])
ax2 = fig.add_subplot(gs1[-1, :-1])
ax3 = fig.add_subplot(gs1[-1, -1])

gs2 = GridSpec(3, 3, left=0.55, right=0.98, hspace=0.05)
ax4 = fig.add_subplot(gs2[:, :-1])
ax5 = fig.add_subplot(gs2[:-1, -1])
ax6 = fig.add_subplot(gs2[-1, -1])
```

### Step 4: Annotate Axes

In this step, we will annotate the axes with their corresponding subplot numbers.

```python
def annotate_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

annotate_axes(fig)
```

### Step 5: Display the Plots

In this step, we will display the plots.

```python
plt.show()
```

## Summary

In this tutorial, we learned how to use `GridSpec` to generate subplots and control the spacing around and between subplots. We also learned how to annotate the axes with their corresponding subplot numbers. These skills will be useful in creating complex plots and visualizations.
