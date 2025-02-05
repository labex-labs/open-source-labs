# Set up the figure and axes

We will create a figure object and set up four axes objects using the `fig.add_axes` method.

```python
fig = plt.figure(figsize=(5.5, 4))
rect = (0.1, 0.1, 0.8, 0.8)
ax = [fig.add_axes(rect, label="%d" % i) for i in range(4)]
```
