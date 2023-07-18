# Matplotlib Tutorial Lab

## Introduction

This tutorial will guide you through the process of creating a plot with annotations using Matplotlib in Python. You will learn how to connect two points with an arrow, add an ellipse to the plot, and customize the arrow style and ellipse properties.

## Steps

### Step 1: Set up the plot

First, we need to set up the plot with two subplots. We will use the `subplots` function to create a 2x2 grid of subplots, and then we will define the x and y coordinates of two points.

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, axs = plt.subplots(2, 2)
x1, y1 = 0.3, 0.3
x2, y2 = 0.7, 0.7
```

### Step 2: Connect two points with an arrow

In this step, we will connect the two points with an arrow. We will use the `annotate` function to create the arrow, and we will customize the arrow style and color.

```python
ax = axs.flat[0]
ax.plot([x1, x2], [y1, y2], ".")
ax.annotate("",
            xy=(x1, y1), xycoords='data',
            xytext=(x2, y2), textcoords='data',
            arrowprops=dict(arrowstyle="-",
                            color="0.5",
                            connectionstyle="arc3,rad=0.3",
                            ),
            )
```

### Step 3: Add an ellipse to the plot

In this step, we will add an ellipse to the plot. We will use the `Ellipse` function to create the ellipse, and we will customize the ellipse properties such as the position, width, height, and angle.

```python
ax = axs.flat[1]
ax.plot([x1, x2], [y1, y2], ".")
el = mpatches.Ellipse((x1, y1), 0.3, 0.4, angle=30, alpha=0.2)
ax.add_artist(el)
```

### Step 4: Customize the arrow to connect to the ellipse

In this step, we will customize the arrow to connect to the ellipse. We will use the `arrowprops` parameter to specify that the arrow should connect to the ellipse, and we will also customize the arrow style and color.

```python
ax = axs.flat[2]
ax.plot([x1, x2], [y1, y2], ".")
el = mpatches.Ellipse((x1, y1), 0.3, 0.4, angle=30, alpha=0.2)
ax.add_artist(el)
ax.annotate("",
            xy=(x1, y1), xycoords='data',
            xytext=(x2, y2), textcoords='data',
            arrowprops=dict(arrowstyle="-",
                            color="0.5",
                            patchB=el,
                            connectionstyle="arc3,rad=0.3",
                            ),
            )
```

### Step 5: Customize the arrow to shrink to the ellipse

In this step, we will customize the arrow to shrink to the ellipse. We will use the `shrinkB` parameter to specify the amount by which the arrow should shrink towards the ellipse.

```python
ax = axs.flat[3]
ax.plot([x1, x2], [y1, y2], ".")
el = mpatches.Ellipse((x1, y1), 0.3, 0.4, angle=30, alpha=0.2)
ax.add_artist(el)
ax.annotate("",
            xy=(x1, y1), xycoords='data',
            xytext=(x2, y2), textcoords='data',
            arrowprops=dict(arrowstyle="fancy",
                            color="0.5",
                            patchB=el,
                            shrinkB=5,
                            connectionstyle="arc3,rad=0.3",
                            ),
            )
```

## Summary

In this tutorial, you learned how to create a plot with annotations using Matplotlib in Python. You learned how to connect two points with an arrow, add an ellipse to the plot, and customize the arrow style and ellipse properties. These skills will be useful in creating informative and visually appealing plots for data visualization.
