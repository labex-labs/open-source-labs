# Create the Figure

Create a Figure object and add a subplot to it. In this example, we're creating a sine wave plot.

```python
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(1, 1, 1)
t = np.arange(0.0, 3.0, 0.01)
s = np.sin(2*np.pi*t)
ax.plot(t, s)
```
