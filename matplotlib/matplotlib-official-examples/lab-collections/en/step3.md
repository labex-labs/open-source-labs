# Create offsets

```python
# Fixing random state for reproducibility
rs = np.random.RandomState(19680801)

# Make some offsets
xyo = rs.randn(npts, 2)
```

The third step is to create offsets using Numpy. We will be using the random function to create the offsets.
