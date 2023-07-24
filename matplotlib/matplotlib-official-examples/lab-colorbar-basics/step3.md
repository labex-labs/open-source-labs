# Create Positive Data Plot and Colorbar

We create a plot of the positive data, and add a colorbar to the plot using the `colorbar` function.

```python
# plot just the positive data and save the
# color "mappable" object returned by ax1.imshow
pos = plt.imshow(Zpos, cmap='Blues', interpolation='none')

# add the colorbar using the figure's method,
# telling which mappable we're talking about and
# which axes object it should be near
plt.colorbar(pos)
```
