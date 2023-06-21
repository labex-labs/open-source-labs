# Custom Box Styles in Matplotlib

## Introduction

Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy. One of the features of Matplotlib is the ability to create customized box styles.

In this lab, you will learn how to implement custom box styles in Matplotlib. You will learn how to create a custom box style as a function and as a class. You will also learn how to register a custom box style with Matplotlib.

## Steps

### Step 1: Implement a custom box style as a function

Custom box styles can be implemented as functions that take arguments specifying both a rectangular box and the amount of "mutation", and return the "mutated" path. Here, we will implement a custom box style that returns a new path which adds an "arrow" shape on the left of the box.

```python
import matplotlib.pyplot as plt
from matplotlib.patches import BoxStyle
from matplotlib.path import Path

def custom_box_style(x0, y0, width, height, mutation_size):
    """
    Given the location and size of the box, return the path of the box around
    it.

    Rotation is automatically taken care of.

    Parameters
    ----------
    x0, y0, width, height : float
        Box location and size.
    mutation_size : float
        Mutation reference scale, typically the text font size.
    """
    # padding
    mypad = 0.3
    pad = mutation_size * mypad
    # width and height with padding added.
    width = width + 2 * pad
    height = height + 2 * pad
    # boundary of the padded box
    x0, y0 = x0 - pad, y0 - pad
    x1, y1 = x0 + width, y0 + height
    # return the new path
    return Path([(x0, y0),
                 (x1, y0), (x1, y1), (x0, y1),
                 (x0-pad, (y0+y1)/2), (x0, y0),
                 (x0, y0)],
                closed=True)

fig, ax = plt.subplots(figsize=(3, 3))
ax.text(0.5, 0.5, "Test", size=30, va="center", ha="center", rotation=30,
        bbox=dict(boxstyle=custom_box_style, alpha=0.2))
plt.show()
```

### Step 2: Implement a custom box style as a class

Custom box styles can also be implemented as classes that implement `__call__`. The classes can then be registered into the `BoxStyle._style_list` dict, which allows specifying the box style as a string, `bbox=dict(boxstyle="registered_name,param=value,...", ...)`.

```python
class MyStyle:
    """A simple box."""

    def __init__(self, pad=0.3):
        """
        The arguments must be floats and have default values.

        Parameters
        ----------
        pad : float
            amount of padding
        """
        self.pad = pad
        super().__init__()

    def __call__(self, x0, y0, width, height, mutation_size):
        """
        Given the location and size of the box, return the path of the box
        around it.

        Rotation is automatically taken care of.

        Parameters
        ----------
        x0, y0, width, height : float
            Box location and size.
        mutation_size : float
            Reference scale for the mutation, typically the text font size.
        """
        # padding
        pad = mutation_size * self.pad
        # width and height with padding added
        width = width + 2.*pad
        height = height + 2.*pad
        # boundary of the padded box
        x0, y0 = x0 - pad, y0 - pad
        x1, y1 = x0 + width, y0 + height
        # return the new path
        return Path([(x0, y0),
                     (x1, y0), (x1, y1), (x0, y1),
                     (x0-pad, (y0+y1)/2.), (x0, y0),
                     (x0, y0)],
                    closed=True)


BoxStyle._style_list["angled"] = MyStyle  # Register the custom style.

fig, ax = plt.subplots(figsize=(3, 3))
ax.text(0.5, 0.5, "Test", size=30, va="center", ha="center", rotation=30,
        bbox=dict(boxstyle="angled,pad=0.5", alpha=0.2))

del BoxStyle._style_list["angled"]  # Unregister it.

plt.show()
```

### Step 3: Register the custom box style with Matplotlib

Once you have implemented a custom box style as a class, you can register it with Matplotlib. This allows you to specify the box style as a string, `bbox=dict(boxstyle="registered_name,param=value,...", ...)`.

```python
BoxStyle._style_list["angled"] = MyStyle  # Register the custom style.
```

### Step 4: Use the custom box style

Once you have implemented and registered a custom box style, you can use it with `Axes.text`.

```python
fig, ax = plt.subplots(figsize=(3, 3))
ax.text(0.5, 0.5, "Test", size=30, va="center", ha="center", rotation=30,
        bbox=dict(boxstyle="angled,pad=0.5", alpha=0.2))
```

## Summary

In this lab, you learned how to implement custom box styles in Matplotlib. You learned how to create a custom box style as a function and as a class. You also learned how to register a custom box style with Matplotlib and how to use it with `Axes.text`.
