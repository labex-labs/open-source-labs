# Plot using `.plot()`

We can achieve the same behavior as `.step()` by using the `drawstyle` parameter of the `.plot()` function. We will create three plots using different values for `drawstyle`.

```python
plt.plot(x, y + 2, drawstyle='steps', label='steps (=steps-pre)')
plt.plot(x, y + 1, drawstyle='steps-mid', label='steps-mid')
plt.plot(x, y, drawstyle='steps-post', label='steps-post')
plt.legend()
plt.show()
```

The above code will create a plot with three piece-wise constant curves, each with a different value for `drawstyle`.
