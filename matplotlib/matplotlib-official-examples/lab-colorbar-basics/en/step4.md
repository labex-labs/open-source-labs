# Create Negative Data Plot and Colorbar

We create a plot of the negative data, and add a colorbar to the plot using the `colorbar` function. This time, we specify the location of the colorbar, as well as the anchor and shrink parameters.

```python
# repeat everything above for the negative data
# you can specify location, anchor and shrink the colorbar
neg = plt.imshow(Zneg, cmap='Reds_r', interpolation='none')
plt.colorbar(neg, location='right', anchor=(0, 0.3), shrink=0.7)
```
