# Matplotlib Patheffect Lab

## Introduction

In this lab, you will learn how to use path effects in Matplotlib to add special effects to your plots. Path effects allow you to add custom strokes, shadows, and other visual effects to your text and plot elements.

## Steps

### Step 1: Import Libraries and Prepare Data

First, we need to import the necessary libraries and prepare some data to plot.

```python
import matplotlib.pyplot as plt
import numpy as np

# Prepare data
arr = np.arange(25).reshape((5, 5))
```

### Step 2: Add Stroke Effect to Text

We can add a stroke effect to text using the `withStroke` path effect. In this example, we will add a stroke effect to the text annotation in the plot.

```python
# Create plot and add text annotation with stroke effect
fig, ax = plt.subplots()
ax.imshow(arr)
txt = ax.annotate("test", (1., 1.), (0., 0),
                   arrowprops=dict(arrowstyle="->",
                                   connectionstyle="angle3", lw=2),
                   size=20, ha="center",
                   path_effects=[patheffects.withStroke(linewidth=3,
                                                        foreground="w")])
txt.arrow_patch.set_path_effects([
    patheffects.Stroke(linewidth=5, foreground="w"),
    patheffects.Normal()])

# Add grid with stroke effect
pe = [patheffects.withStroke(linewidth=3,
                             foreground="w")]
ax.grid(True, linestyle="-", path_effects=pe)

plt.show()
```

### Step 3: Add Stroke Effect to Contour Lines

We can also add stroke effects to contour lines and their labels using the `withStroke` path effect.

```python
# Create plot and add contour lines with stroke effect
fig, ax = plt.subplots()
ax.imshow(arr)
cntr = ax.contour(arr, colors="k")

plt.setp(cntr.collections, path_effects=[
    patheffects.withStroke(linewidth=3, foreground="w")])

clbls = ax.clabel(cntr, fmt="%2.0f", use_clabeltext=True)
plt.setp(clbls, path_effects=[
    patheffects.withStroke(linewidth=3, foreground="w")])

plt.show()
```

### Step 4: Add Shadow Effect to Legend

We can add a shadow effect to a legend using the `withSimplePatchShadow` path effect.

```python
# Create plot and add shadow effect to legend
fig, ax = plt.subplots()
p1, = ax.plot([0, 1], [0, 1])
leg = ax.legend([p1], ["Line 1"], fancybox=True, loc='upper left')
leg.legendPatch.set_path_effects([patheffects.withSimplePatchShadow()])

plt.show()
```

## Summary

In this lab, you learned how to use path effects in Matplotlib to add special effects to your plots. You learned how to add stroke effects to text, contour lines, and their labels, as well as how to add a shadow effect to a legend. With path effects, you can create visually stunning plots that convey your data in a clear and concise way.
