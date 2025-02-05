# Create Plot with Positive and Negative Data

We create a plot with both positive and negative data, and add a colorbar to the plot using the `colorbar` function. This time, we specify the minimum and maximum values for the colorbar using the `vmin` and `vmax` parameters.

```python
# Plot both positive and negative values between +/- 1.2
pos_neg_clipped = plt.imshow(Z, cmap='RdBu', vmin=-1.2, vmax=1.2,
                             interpolation='none')

# Add minorticks on the colorbar to make it easy to read the
# values off the colorbar.
cbar = plt.colorbar(pos_neg_clipped, extend='both')
cbar.minorticks_on()
```
