# Create the Figure and Subplots

The second step is to create the figure and subplots that will be used for the animation. In this example, we create two subplots side-by-side with different aspect ratios. The left subplot is a unit circle, and the right subplot is an empty plot that will be used to animate a sine curve.

```python
fig, (axl, axr) = plt.subplots(
    ncols=2,
    sharey=True,
    figsize=(6, 2),
    gridspec_kw=dict(width_ratios=[1, 3], wspace=0),
)
axl.set_aspect(1)
axr.set_box_aspect(1 / 3)
axr.yaxis.set_visible(False)
axr.xaxis.set_ticks([0, np.pi, 2 * np.pi], ["0", r"$\pi$", r"$2\pi$"])
```
