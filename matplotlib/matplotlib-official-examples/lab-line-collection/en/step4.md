# Create Plot

We can now create a plot using `matplotlib` and add the `LineCollection` object to the plot using the `add_collection` method of the `Axes` object.

```python
fig, ax = plt.subplots()
ax.set_xlim(x.min(), x.max())
ax.set_ylim(ys.min(), ys.max())

ax.add_collection(line_segments)
ax.set_title('Line collection with masked arrays')
plt.show()
```
