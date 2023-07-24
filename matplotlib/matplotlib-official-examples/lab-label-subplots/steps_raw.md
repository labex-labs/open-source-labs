# Labelling Subplots with Matplotlib

## Introduction

Matplotlib is a widely used data visualization library in Python. It provides a variety of tools to create different types of plots, including subplots. When creating subplots, it is often helpful to label each plot to make it easier for the reader to understand the information being presented. In this lab, we will learn how to label subplots using different methods provided by Matplotlib.

## Steps

### Step 1: Import Libraries

The first step is to import the required libraries. We will be using `matplotlib.pyplot` and `matplotlib.transforms` to create and transform the subplots.

```python
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
```

### Step 2: Create Subplots

Next, we create the subplots using `plt.subplot_mosaic`. We will create a 3x2 grid of subplots and label them as follows:

- The top-left plot will be labeled as "a)"
- The bottom-left plot will be labeled as "b)"
- The top-right and bottom-right plots will be labeled as "c)" and "d)" respectively.

```python
fig, axs = plt.subplot_mosaic([['a)', 'c)'], ['b)', 'c)'], ['d)', 'd)']], layout='constrained')
```

### Step 3: Label Inside the Axes

The simplest method to label subplots is to put the label inside the axes. We can achieve this by using the `ax.text` method. We will loop through each subplot and add the label inside the axes using `ax.transAxes`.

```python
for label, ax in axs.items():
    # label physical distance in and down:
    trans = mtransforms.ScaledTranslation(10/72, -5/72, fig.dpi_scale_trans)
    ax.text(0.0, 1.0, label, transform=ax.transAxes + trans,
            fontsize='medium', verticalalignment='top', fontfamily='serif',
            bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
```

### Step 4: Label Outside the Axes

We may prefer the labels outside the axes but still aligned with each other. In this case, we use a slightly different transform.

```python
for label, ax in axs.items():
    # label physical distance to the left and up:
    trans = mtransforms.ScaledTranslation(-20/72, 7/72, fig.dpi_scale_trans)
    ax.text(0.0, 1.0, label, transform=ax.transAxes + trans,
            fontsize='medium', va='bottom', fontfamily='serif')
```

### Step 5: Label with Title

If we want the label to be aligned with the title, we can incorporate it into the title or use the `loc` keyword argument.

```python
for label, ax in axs.items():
    ax.set_title('Normal Title', fontstyle='italic')
    ax.set_title(label, fontfamily='serif', loc='left', fontsize='medium')
```

### Step 6: Display the Subplots

Finally, we display the subplots using `plt.show()`.

```python
plt.show()
```

## Summary

In this lab, we learned how to label subplots in Matplotlib using different methods. We used `ax.text` to label inside the axes, `ax.set_title` to label with the title, and `plt.subplot_mosaic` to create the subplots. We also used `matplotlib.transforms` to transform the axes to align the labels. By labeling the subplots, we can make our plots more informative and easier to understand.
