# Add data to the plot

Finally, you can add some data to the plot to visualize it. In this case, you can use the `plot()` function to plot a sine wave.

```python
x = np.linspace(-0.5, 1., 100)
ax.plot(x, np.sin(x*np.pi))
```
