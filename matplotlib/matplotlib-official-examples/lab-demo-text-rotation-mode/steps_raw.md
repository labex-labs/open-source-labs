# Matplotlib Text Rotation Lab

## Introduction

In this lab, you will learn how to rotate text in Matplotlib using the `rotation_mode` parameter. The `rotation_mode` parameter determines the order of rotation and alignment of the text. There are two modes available: `default` and `anchor`.

## Steps

### Step 1: Import the necessary libraries

First, we need to import the necessary libraries. In this lab, we will use Matplotlib to create the plots.

```python
import matplotlib.pyplot as plt
```

### Step 2: Define the `test_rotation_mode` function

We will create a function called `test_rotation_mode` that will create subplots to test the different rotation modes. It takes two parameters: `fig` and `mode`.

```python
def test_rotation_mode(fig, mode):
```

### Step 3: Define the horizontal and vertical alignment lists

Next, we will define the horizontal and vertical alignment lists that will be used to create the subplots. We will create three elements for each list: `"left"`, `"center"`, and `"right"` for horizontal alignment, and `"top"`, `"center"`, and `"bottom"` for vertical alignment.

```python
ha_list = ["left", "center", "right"]
va_list = ["top", "center", "baseline", "bottom"]
```

### Step 4: Create the subplots

Now, we will create the subplots using the `subplots` function. We will create a grid of subplots with the same aspect ratio, and we will remove the ticks from the x and y axes. We will also add a vertical and horizontal line at the center of each subplot to help visualize the alignment.

```python
axs = fig.subplots(len(va_list), len(ha_list), sharex=True, sharey=True,
                   subplot_kw=dict(aspect=1),
                   gridspec_kw=dict(hspace=0, wspace=0))

for i, va in enumerate(va_list):
    for j, ha in enumerate(ha_list):
        ax = axs[i, j]
        ax.set(xticks=[], yticks=[])
        ax.axvline(0.5, color="skyblue", zorder=0)
        ax.axhline(0.5, color="skyblue", zorder=0)
        ax.plot(0.5, 0.5, color="C0", marker="o", zorder=1)
```

### Step 5: Add text to the subplots

We will add text to each subplot using the `text` function. We will use the parameters `rotation`, `horizontalalignment`, `verticalalignment`, and `rotation_mode` to rotate and align the text. We will also use the `bbox` parameter to highlight the bounding box of the text.

```python
kw = (
    {} if mode == "default" else
    {"bbox": dict(boxstyle="square,pad=0.", ec="none", fc="C1", alpha=0.3)}
)

texts = {}

for i, va in enumerate(va_list):
    for j, ha in enumerate(ha_list):
        ax = axs[i, j]
        tx = ax.text(0.5, 0.5, "Tpg",
                     size="x-large", rotation=40,
                     horizontalalignment=ha, verticalalignment=va,
                     rotation_mode=mode, **kw)
        texts[ax] = tx
```

### Step 6: Highlight the bounding box of the text

If the `rotation_mode` is set to `'default'`, we will highlight the bounding box of the text using a rectangle. We will use the `get_window_extent` function to get the bounding box and transform it to the data coordinates using the `transData` attribute.

```python
if mode == "default":
    fig.canvas.draw()
    for ax, text in texts.items():
        bb = text.get_window_extent().transformed(ax.transData.inverted())
        rect = plt.Rectangle((bb.x0, bb.y0), bb.width, bb.height,
                             facecolor="C1", alpha=0.3, zorder=2)
        ax.add_patch(rect)
```

### Step 7: Create the subfigures and call the `test_rotation_mode` function

We will create two subfigures and call the `test_rotation_mode` function with the `fig` and `mode` parameters.

```python
fig = plt.figure(figsize=(8, 5))
subfigs = fig.subfigures(1, 2)
test_rotation_mode(subfigs[0], "default")
test_rotation_mode(subfigs[1], "anchor")
plt.show()
```

## Summary

In this lab, we learned how to rotate text in Matplotlib using the `rotation_mode` parameter. We created a function called `test_rotation_mode` that created subplots to test the different rotation modes. We defined the horizontal and vertical alignment lists, created the subplots, added text to the subplots, and highlighted the bounding box of the text. Finally, we created the subfigures and called the `test_rotation_mode` function.
