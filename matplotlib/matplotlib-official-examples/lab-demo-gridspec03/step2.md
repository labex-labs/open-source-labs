# Generate Subplots with `GridSpec`

In this step, we will use `GridSpec` to generate subplots. We will create a figure with 2 rows and 2 columns. We will also specify the `width_ratios` and `height_ratios` to control the relative sizes of the subplots.

```python
fig = plt.figure()
gs = GridSpec(2, 2, width_ratios=[1, 2], height_ratios=[4, 1])
ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])
ax3 = fig.add_subplot(gs[2])
ax4 = fig.add_subplot(gs[3])
```
