# Add a colorbar to the plot

Now, we will add a colorbar to each subplot using Matplotlib's `make_axes_locatable` function. This function takes an existing axes, adds it to a new `AxesDivider` and returns the `AxesDivider`. The `append_axes` method of the `AxesDivider` can then be used to create a new axes on a given side ("top", "right", "bottom", or "left") of the original axes.

```python
ax1_divider = make_axes_locatable(ax1)
cax1 = ax1_divider.append_axes("right", size="7%", pad="2%")
cb1 = fig.colorbar(im1, cax=cax1)

ax2_divider = make_axes_locatable(ax2)
cax2 = ax2_divider.append_axes("top", size="7%", pad="2%")
cb2 = fig.colorbar(im2, cax=cax2, orientation="horizontal")
cax2.xaxis.set_ticks_position("top")
```
