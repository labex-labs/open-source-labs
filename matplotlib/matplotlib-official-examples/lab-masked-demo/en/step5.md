# Set to NaN

We will set to NaN where y > 0.7. We will create a new y array with NaN values.

```python
y4 = y.copy()
y4[y3 > 0.7] = np.nan
```
