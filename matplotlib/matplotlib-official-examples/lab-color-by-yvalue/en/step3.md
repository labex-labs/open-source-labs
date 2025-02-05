# Create Masked Arrays

In this step, we will create three masked arrays: one for values greater than a certain threshold, one for values less than a certain threshold, and one for values between two thresholds.

```python
upper = 0.77
lower = -0.77

supper = np.ma.masked_where(s < upper, s)
slower = np.ma.masked_where(s > lower, s)
smiddle = np.ma.masked_where((s < lower) | (s > upper), s)
```
