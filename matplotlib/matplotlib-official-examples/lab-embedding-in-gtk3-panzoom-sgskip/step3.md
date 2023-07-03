# Create a Matplotlib Figure and Plot Data

Now, we will create a Matplotlib figure with a subplot and plot data on it.

```python
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(1, 1, 1)
t = np.arange(0.0, 3.0, 0.01)
s = np.sin(2*np.pi*t)
ax.plot(t, s)
```
