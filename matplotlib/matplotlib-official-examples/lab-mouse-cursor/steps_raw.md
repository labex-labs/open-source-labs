# Python Matplotlib Tutorial: Alternative Cursor

## Introduction

This lab will guide you on how to set an alternative cursor on a figure canvas using Matplotlib. The alternative cursor can be any of the available cursors in the Matplotlib backend tools.

## Steps

### Step 1: Import the necessary libraries

First, we need to import the required libraries. We will be using `matplotlib.pyplot` and `matplotlib.backend_tools`.

```python
import matplotlib.pyplot as plt
from matplotlib.backend_tools import Cursors
```

### Step 2: Create a figure and set alternative cursors

Next, we create a figure and set the alternative cursors for each subplot using a loop. We also add text to each subplot to indicate the cursor being used.

```python
fig, axs = plt.subplots(len(Cursors), figsize=(6, len(Cursors) + 0.5), gridspec_kw={'hspace': 0})
fig.suptitle('Hover over an Axes to see alternate Cursors')

for cursor, ax in zip(Cursors, axs):
    ax.cursor_to_use = cursor
    ax.text(0.5, 0.5, cursor.name,
            horizontalalignment='center', verticalalignment='center')
    ax.set(xticks=[], yticks=[])
```

### Step 3: Set the cursor on hover

We need to set the cursor to the alternative cursor when the user hovers over a subplot. We achieve this using the `motion_notify_event` event and the `set_cursor()` function.

```python
def hover(event):
    if fig.canvas.widgetlock.locked():
        # Don't do anything if the zoom/pan tools have been enabled.
        return

    fig.canvas.set_cursor(
        event.inaxes.cursor_to_use if event.inaxes else Cursors.POINTER)

fig.canvas.mpl_connect('motion_notify_event', hover)
```

### Step 4: Display the figure

Finally, we display the figure using the `show()` function.

```python
plt.show()
```

## Summary

In this lab, we have learned how to set an alternative cursor on a figure canvas using Matplotlib. We created a figure and set the alternative cursors for each subplot, and then set the cursor to the alternative cursor when the user hovers over a subplot. We then displayed the figure.
