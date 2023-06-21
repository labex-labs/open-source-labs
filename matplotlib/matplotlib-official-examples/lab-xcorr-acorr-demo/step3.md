# Plot Cross-Correlation

We will now plot the cross-correlation between the two arrays using the `xcorr` function in Matplotlib.

```python
fig, ax = plt.subplots()
ax.xcorr(x, y, usevlines=True, maxlags=50, normed=True, lw=2)
ax.grid(True)
plt.show()
```

The `xcorr` function takes the following parameters:

- `x`: the first array of data
- `y`: the second array of data
- `usevlines`: boolean, whether to plot vertical lines from 0 to the correlation value
- `maxlags`: integer, the maximum number of lags to calculate the correlation for
- `normed`: boolean, whether to normalize the correlation values
- `lw`: integer, the line width for the plot

#
