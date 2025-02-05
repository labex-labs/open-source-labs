# Mask Points

We will mask points where y > 0.7 using a masked array. We will create a new y array with masked values.

```python
y3 = np.ma.masked_where(y > 0.7, y)
```
