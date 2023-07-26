# Create the Second Plot

Next, we will create the second plot. We will use `subplot` again, but this time we will set the `sharex` attribute to the first plot (`ax1`). This ensures that the second plot will share the same x-axis as the first plot.

```python
ax2 = plt.subplot(212, sharex=ax1)
ax2.plot(t, np.sin(4*np.pi*t))
```
