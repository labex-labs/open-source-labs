# Step-by-Step Lab: Adding Angle Annotations to Bracket Arrows in Matplotlib

## Introduction

In this lab, you will learn how to add angle annotations to bracket arrow styles created using `FancyArrowPatch` in Matplotlib. Angle annotations are useful for indicating the direction and size of angles in a plot. By the end of this lab, you will be able to create bracket arrow styles with angle annotations and customize them to fit your specific needs.

## Steps

### Step 1: Import necessary libraries and set up plot

First, we need to import the necessary libraries and set up the plot. We will be using `matplotlib.pyplot` and `numpy`. We will also create a figure and an axis object to plot our data on.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import FancyArrowPatch

fig, ax = plt.subplots()
ax.set(xlim=(0, 6), ylim=(-1, 5))
ax.set_title("Orientation of the bracket arrows relative to angleA and angleB")
```

### Step 2: Define a function to get the point of a rotated vertical line

We will define a function that takes the origin coordinates, line length, and angle in degrees as inputs and returns the xy coordinates of the vertical line end rotated by the specified angle.

```python
def get_point_of_rotated_vertical(origin, line_length, degrees):
    """Return xy coordinates of the vertical line end rotated by degrees."""
    rad = np.deg2rad(-degrees)
    return [origin[0] + line_length * np.sin(rad),
            origin[1] + line_length * np.cos(rad)]
```

### Step 3: Create bracket arrows with angle annotations

We will create three bracket arrow styles with angle annotations using `FancyArrowPatch`. Each bracket arrow will have a different angle value for _angleA_ and _angleB_. We will also add vertical lines to indicate the position of the angle annotations.

```python
style = ']-['
for i, angle in enumerate([-40, 0, 60]):
    y = 2*i
    arrow_centers = ((1, y), (5, y))
    vlines = ((1, y + 0.5), (5, y + 0.5))
    anglesAB = (angle, -angle)
    bracketstyle = f"{style}, angleA={anglesAB[0]}, angleB={anglesAB[1]}"
    bracket = FancyArrowPatch(*arrow_centers, arrowstyle=bracketstyle,
                              mutation_scale=42)
    ax.add_patch(bracket)
    ax.text(3, y + 0.05, bracketstyle, ha="center", va="bottom", fontsize=14)
    ax.vlines([line[0] for line in vlines], [y, y], [line[1] for line in vlines],
              linestyles="--", color="C0")
```

### Step 4: Add angle annotation arrows and text

We will add angle annotation arrows and text to each bracket arrow style. First, we will get the top coordinates for the drawn patches at _angleA_ and _angleB_. Then, we will define the connection directions for the annotation arrows. Finally, we will add arrows and annotation text to the plot.

```python
    # Get the top coordinates for the drawn patches at A and B
    patch_tops = [get_point_of_rotated_vertical(center, 0.5, angle)
                  for center, angle in zip(arrow_centers, anglesAB)]
    # Define the connection directions for the annotation arrows
    connection_dirs = (1, -1) if angle > 0 else (-1, 1)
    # Add arrows and annotation text
    arrowstyle = "Simple, tail_width=0.5, head_width=4, head_length=8"
    for vline, dir, patch_top, angle in zip(vlines, connection_dirs,
                                            patch_tops, anglesAB):
        kw = dict(connectionstyle=f"arc3,rad={dir * 0.5}",
                  arrowstyle=arrowstyle, color="C0")
        ax.add_patch(FancyArrowPatch(vline, patch_top, **kw))
        ax.text(vline[0] - dir * 0.15, y + 0.7, f'{angle}°', ha="center",
                va="center")
```

### Step 5: Display the plot

We will display the plot using `plt.show()`.

```python
plt.show()
```

## Summary

In this lab, you learned how to add angle annotations to bracket arrow styles created using `FancyArrowPatch` in Matplotlib. You also learned how to customize the bracket arrow styles to fit your specific needs. By following the step-by-step instructions and sample code provided, you should now be able to create bracket arrow styles with angle annotations in your own Matplotlib plots.
