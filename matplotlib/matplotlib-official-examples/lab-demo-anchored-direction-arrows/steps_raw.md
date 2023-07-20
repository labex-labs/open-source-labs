# Matplotlib Anchored Direction Arrow Lab

## Introduction

In this lab, we will learn how to create anchored direction arrows in Matplotlib. Anchored direction arrows are arrows that point in a specific direction and are anchored to a plot. These arrows are useful for indicating specific directions or orientations in a plot. We will learn how to create simple arrows as well as high contrast and rotated arrows.

## Steps

### Step 1: Import necessary libraries

First, we need to import necessary libraries such as Matplotlib, NumPy, Matplotlib font manager, and AnchoredDirectionArrows from mpl_toolkits.axes_grid1. We will use these libraries to create anchored direction arrows.

```python
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.font_manager as fm
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredDirectionArrows
```

### Step 2: Create a plot

Next, we will create a simple plot using NumPy. This plot will serve as a background for the anchored direction arrows.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

fig, ax = plt.subplots()
ax.imshow(np.random.random((10, 10)))
```

### Step 3: Create a simple arrow

Now, we will create a simple anchored direction arrow using the AnchoredDirectionArrows class. This arrow will indicate the X and Y directions in the plot.

```python
# Simple example
simple_arrow = AnchoredDirectionArrows(ax.transAxes, 'X', 'Y')
ax.add_artist(simple_arrow)
```

### Step 4: Create a high contrast arrow

Next, we will create a high contrast anchored direction arrow. This arrow will have a white outline and a black fill.

```python
high_contrast_part_1 = AnchoredDirectionArrows(
                            ax.transAxes,
                            '111', r'11$\overline{2}$',
                            loc='upper right',
                            arrow_props={'ec': 'w', 'fc': 'none', 'alpha': 1,
                                         'lw': 2}
                            )
ax.add_artist(high_contrast_part_1)

high_contrast_part_2 = AnchoredDirectionArrows(
                            ax.transAxes,
                            '111', r'11$\overline{2}$',
                            loc='upper right',
                            arrow_props={'ec': 'none', 'fc': 'k'},
                            text_props={'ec': 'w', 'fc': 'k', 'lw': 0.4}
                            )
ax.add_artist(high_contrast_part_2)
```

### Step 5: Create a rotated arrow

In this step, we will create a rotated anchored direction arrow. This arrow will be rotated by 30 degrees and will have a serif font.

```python
fontprops = fm.FontProperties(family='serif')

rotated_arrow = AnchoredDirectionArrows(
                    ax.transAxes,
                    '30', '120',
                    loc='center',
                    color='w',
                    angle=30,
                    fontproperties=fontprops
                    )
ax.add_artist(rotated_arrow)
```

### Step 6: Alter the arrow directions

In this step, we will create three anchored direction arrows that point in different directions. These arrows will have different lengths and aspect ratios.

```python
a1 = AnchoredDirectionArrows(
        ax.transAxes, 'A', 'B', loc='lower center',
        length=-0.15,
        sep_x=0.03, sep_y=0.03,
        color='r'
    )
ax.add_artist(a1)

a2 = AnchoredDirectionArrows(
        ax.transAxes, 'A', ' B', loc='lower left',
        aspect_ratio=-1,
        sep_x=0.01, sep_y=-0.02,
        color='orange'
        )
ax.add_artist(a2)


a3 = AnchoredDirectionArrows(
        ax.transAxes, ' A', 'B', loc='lower right',
        length=-0.15,
        aspect_ratio=-1,
        sep_y=-0.1, sep_x=0.04,
        color='cyan'
        )
ax.add_artist(a3)
```

### Step 7: Display the plot

Finally, we will display the plot with all the anchored direction arrows.

```python
plt.show()
```

## Summary

In this lab, we learned how to create anchored direction arrows in Matplotlib. We created simple arrows as well as high contrast and rotated arrows. We also learned how to alter the arrow directions and aspect ratios. Anchored direction arrows are useful for indicating specific directions or orientations in a plot.
