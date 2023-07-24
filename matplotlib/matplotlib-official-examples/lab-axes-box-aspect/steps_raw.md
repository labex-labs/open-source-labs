# Matplotlib Box Aspect Lab

## Introduction

This lab will guide you through the process of creating different plots using the `set_box_aspect()` method in Matplotlib. This method sets the aspect ratio between axes height and width in physical units, independent of data limits. It is useful for producing square plots, independent of the data it contains, or to have a usual plot with the same axes dimensions next to an image plot with fixed (data-)aspect.

## Steps

### Step 1: A Square Axes, Independent of Data

We will produce a square axes, no matter what the data limits are.

```python
import matplotlib.pyplot as plt
import numpy as np

fig1, ax = plt.subplots()

ax.set_xlim(300, 400)
ax.set_box_aspect(1)

plt.show()
```

### Step 2: Shared Square Axes

We will produce shared subplots that are squared in size.

```python
fig2, (ax, ax2) = plt.subplots(ncols=2, sharey=True)

ax.plot([1, 5], [0, 10])
ax2.plot([100, 500], [10, 15])

ax.set_box_aspect(1)
ax2.set_box_aspect(1)

plt.show()
```

### Step 3: Square Twin Axes

We will produce a square axes, with a twin axes. The twinned axes takes over the box aspect of the parent.

```python
fig3, ax = plt.subplots()

ax2 = ax.twinx()

ax.plot([0, 10])
ax2.plot([12, 10])

ax.set_box_aspect(1)

plt.show()
```

### Step 4: Normal Plot Next to Image

When creating an image plot with fixed data aspect and the default `adjustable="box"` next to a normal plot, the axes would be unequal in height. `set_box_aspect()` provides an easy solution to that by allowing to have the normal plot's axes use the images dimensions as box aspect. This example also shows that _constrained layout_ interplays nicely with a fixed box aspect.

```python
fig4, (ax, ax2) = plt.subplots(ncols=2, layout="constrained")

np.random.seed(19680801)  # Fixing random state for reproducibility
im = np.random.rand(16, 27)
ax.imshow(im)

ax2.plot([23, 45])
ax2.set_box_aspect(im.shape[0]/im.shape[1])

plt.show()
```

### Step 5: Square Joint/Marginal Plot

It may be desirable to show marginal distributions next to a plot of joint data. The following creates a square plot with the box aspect of the marginal axes being equal to the width- and height-ratios of the gridspec. This ensures that all axes align perfectly, independent on the size of the figure.

```python
fig5, axs = plt.subplots(2, 2, sharex="col", sharey="row",
                         gridspec_kw=dict(height_ratios=[1, 3],
                                          width_ratios=[3, 1]))
axs[0, 1].set_visible(False)
axs[0, 0].set_box_aspect(1/3)
axs[1, 0].set_box_aspect(1)
axs[1, 1].set_box_aspect(3/1)

np.random.seed(19680801)  # Fixing random state for reproducibility
x, y = np.random.randn(2, 400) * [[.5], [180]]
axs[1, 0].scatter(x, y)
axs[0, 0].hist(x)
axs[1, 1].hist(y, orientation="horizontal")

plt.show()
```

### Step 6: Box Aspect for Many Subplots

It is possible to pass the box aspect to an Axes at initialization. The following creates a 2 by 3 subplot grid with all square Axes.

```python
fig7, axs = plt.subplots(2, 3, subplot_kw=dict(box_aspect=1),
                         sharex=True, sharey=True, layout="constrained")

for i, ax in enumerate(axs.flat):
    ax.scatter(i % 3, -((i // 3) - 0.5)*200, c=[plt.cm.hsv(i / 6)], s=300)
plt.show()
```

## Summary

This lab provided an overview of how to use `set_box_aspect()` in Matplotlib to create different types of plots with a fixed aspect ratio between axes height and width.
