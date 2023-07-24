# Plot Data on Subfigures

To plot data on the subfigures, you need to create a subplot for each subfigure using `subfig.subplots()`. Then, you can use any of the plotting functions in Matplotlib to create the plots.

```python
ax1 = subfigs[0].subplots()
ax1.plot(np.arange(10), np.random.randn(10))

ax2 = subfigs[1].subplots()
ax2.plot(np.arange(10), np.random.randn(10))
```

This will create two subfigures, each with a plot of random data.
