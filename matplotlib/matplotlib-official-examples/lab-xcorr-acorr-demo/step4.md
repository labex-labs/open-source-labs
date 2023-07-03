# Plot Auto-Correlation

We will now plot the auto-correlation of the `x` array using the `acorr` function in Matplotlib.

```python
fig, ax = plt.subplots()
ax.acorr(x, usevlines=True, normed=True, maxlags=50, lw=2)
ax.grid(True)
plt.show()
```

The `acorr` function takes the following parameters:

- `x`: the array of data to calculate the auto-correlation for
- `usevlines`: boolean, whether to plot vertical lines from 0 to the correlation value
- `normed`: boolean, whether to normalize the correlation values
- `maxlags`: integer, the maximum number of lags to calculate the correlation for
- `lw`: integer, the line width for the plot
