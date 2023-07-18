# Drawing Fancy Boxes with Matplotlib

## Introduction

Matplotlib is a popular data visualization library in Python. This lab will guide you through the process of creating fancy boxes with different visual properties.

## Steps

### Step 1: Import libraries and get box styles

In this step, we will import the necessary libraries and get the box styles that we will use for plotting.

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch
from matplotlib.patches import FancyBboxPatch
import matplotlib.transforms as mtransforms
import inspect

styles = mpatch.BoxStyle.get_styles()
```

### Step 2: Plot sample boxes with fancybox

In this step, we will plot sample boxes with fancybox using the box styles that we got in step 1.

```python
ncol = 2
nrow = (len(styles) + 1) // ncol
axs = (plt.figure(figsize=(3 * ncol, 1 + nrow))
       .add_gridspec(1 + nrow, ncol, wspace=.5).subplots())

for ax in axs.flat:
    ax.set_axis_off()

for ax in axs[0, :]:
    ax.text(.2, .5, "boxstyle",
            transform=ax.transAxes, size="large", color="tab:blue",
            horizontalalignment="right", verticalalignment="center")
    ax.text(.4, .5, "default parameters",
            transform=ax.transAxes,
            horizontalalignment="left", verticalalignment="center")

for ax, (stylename, stylecls) in zip(axs[1:, :].T.flat, styles.items()):
    ax.text(.2, .5, stylename, bbox=dict(boxstyle=stylename, fc="w", ec="k"),
            transform=ax.transAxes, size="large", color="tab:blue",
            horizontalalignment="right", verticalalignment="center")
    ax.text(.4, .5, str(inspect.signature(stylecls))[1:-1].replace(", ", "\n"),
            transform=ax.transAxes,
            horizontalalignment="left", verticalalignment="center")
```

### Step 3: Show multiple fancy boxes at once

In this step, we will show multiple fancy boxes at once with different visual properties.

```python
def add_fancy_patch_around(ax, bb, **kwargs):
    fancy = FancyBboxPatch(bb.p0, bb.width, bb.height,
                           fc=(1, 0.8, 1, 0.5), ec=(1, 0.5, 1, 0.5),
                           **kwargs)
    ax.add_patch(fancy)
    return fancy


def draw_control_points_for_patches(ax):
    for patch in ax.patches:
        patch.axes.plot(*patch.get_path().vertices.T, ".",
                        c=patch.get_edgecolor())


fig, axs = plt.subplots(2, 2, figsize=(8, 8))

bb = mtransforms.Bbox([[0.3, 0.4], [0.7, 0.6]])

ax = axs[0, 0]
fancy = add_fancy_patch_around(ax, bb, boxstyle="round,pad=0.1")
ax.set(xlim=(0, 1), ylim=(0, 1), aspect=1,
       title='boxstyle="round,pad=0.1"')

ax = axs[0, 1]
fancy = add_fancy_patch_around(ax, bb, boxstyle="round,pad=0.1")
fancy.set_boxstyle("round,pad=0.1,rounding_size=0.2")
ax.set(xlim=(0, 1), ylim=(0, 1), aspect=1,
       title='boxstyle="round,pad=0.1,rounding_size=0.2"')

ax = axs[1, 0]
fancy = add_fancy_patch_around(
    ax, bb, boxstyle="round,pad=0.1", mutation_scale=2)
ax.set(xlim=(0, 1), ylim=(0, 1), aspect=1,
       title='boxstyle="round,pad=0.1"\n mutation_scale=2')

ax = axs[1, 1]
fancy = add_fancy_patch_around(ax, bb, boxstyle="round,pad=0.2")
fancy.set(facecolor="none", edgecolor="green")
fancy = add_fancy_patch_around(
    ax, bb, boxstyle="round,pad=0.3", mutation_aspect=0.5)
ax.set(xlim=(-.5, 1.5), ylim=(0, 1), aspect=2,
       title='boxstyle="round,pad=0.3"\nmutation_aspect=.5')

for ax in axs.flat:
    draw_control_points_for_patches(ax)
    fancy = add_fancy_patch_around(ax, bb, boxstyle="square,pad=0")
    fancy.set(edgecolor="black", facecolor="none", zorder=10)

fig.tight_layout()

plt.show()
```

### Step 4: Conclusion

In this lab, we learned how to create fancy boxes with different visual properties using Matplotlib.

## Summary

Matplotlib is a popular data visualization library in Python. We can create fancy boxes with different visual properties using the FancyBboxPatch class in Matplotlib. By modifying the boxstyle and its attributes, we can create different types of fancy boxes that suit our needs.
