# Plot Data

Now that we have created our subplots, we can plot our data using `np.sin(x)`.

```python
x = np.arange(0, 2*np.pi, 0.01)
ax0.plot(x, np.sin(x))
ax1.plot(x, np.sin(x))
```
