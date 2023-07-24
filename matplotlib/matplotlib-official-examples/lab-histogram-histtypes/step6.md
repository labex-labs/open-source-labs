# Create a histogram with custom bin widths

We can create a histogram with custom and unequal bin widths by providing a list of bin edges. In this example, we will create a histogram with unevenly spaced bins.

```python
bins = [100, 150, 180, 195, 205, 220, 250, 300]
plt.hist(x, bins=bins, density=True, histtype='bar', rwidth=0.8)
plt.show()
```
