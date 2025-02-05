# Plot a 2D Histogram

To plot a 2D histogram, one only needs two vectors of the same length, corresponding to each axis of the histogram.

```python
fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(dist1, dist2)

plt.show()
```
