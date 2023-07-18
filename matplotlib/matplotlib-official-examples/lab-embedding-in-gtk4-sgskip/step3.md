# Create a Matplotlib figure and plot

```python
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot()
t = np.arange(0.0, 3.0, 0.01)
s = np.sin(2*np.pi*t)
ax.plot(t, s)
```

We create a Matplotlib figure with a size of 5x4 inches and a dpi of 100. We then create a subplot and plot a sine wave.
