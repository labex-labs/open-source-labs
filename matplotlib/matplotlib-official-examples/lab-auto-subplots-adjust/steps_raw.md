# Programmatically controlling subplot adjustment

## Introduction

Matplotlib is a powerful library for creating visualizations in Python. Sometimes, when creating plots, you may need to adjust the subplot parameters manually. This lab will show you how to programmatically adjust subplot parameters based on the size of the labels.

## Steps

### Step 1: Import the necessary libraries

We will need `matplotlib.pyplot` and `matplotlib.transforms` to create the plot and manipulate the subplot parameters.

```python
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
```

### Step 2: Create the plot

Let's create a simple line plot with some long y-labels.

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.set_yticks([2, 5, 7], labels=['really, really, really', 'long', 'labels'])
```

### Step 3: Define the draw callback function

We will define a function that will be called every time the plot is drawn. This function will calculate the bounding boxes of the y-labels, determine if the subplot leaves enough room for the labels, and adjust the subplot parameters if necessary.

```python
def on_draw(event):
    bboxes = []
    for label in ax.get_yticklabels():
        # Bounding box in pixels
        bbox_px = label.get_window_extent()
        # Transform to relative figure coordinates. This is the inverse of
        # transFigure.
        bbox_fig = bbox_px.transformed(fig.transFigure.inverted())
        bboxes.append(bbox_fig)
    # the bbox that bounds all the bboxes, again in relative figure coords
    bbox = mtransforms.Bbox.union(bboxes)
    if fig.subplotpars.left < bbox.width:
        # Move the subplot left edge more to the right
        fig.subplots_adjust(left=1.1*bbox.width)  # pad a little
        fig.canvas.draw()
```

### Step 4: Connect the draw event to the callback function

We need to connect the `draw_event` to our `on_draw` function.

```python
fig.canvas.mpl_connect('draw_event', on_draw)
```

### Step 5: Show the plot

Finally, we will show the plot.

```python
plt.show()
```

## Summary

In this lab, we learned how to programmatically adjust subplot parameters based on the size of the labels. We used the `matplotlib.transforms` module to calculate the bounding boxes of the labels and the `draw_event` to call our `on_draw` function.
