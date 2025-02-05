# Plot using `.step()`

We can use the `.step()` function to create piece-wise constant curves. The `where` parameter determines where the steps should be drawn. We will create three plots using different values for `where`.

```python
plt.step(x, y + 2, label='pre (default)', where='pre')
plt.step(x, y + 1, label='mid', where='mid')
plt.step(x, y, label='post', where='post')
plt.legend()
plt.show()
```

The above code will create a plot with three piece-wise constant curves, each with a different value for `where`.
