# Understanding Differences with NumPy

Pandas and NumPy have slight differences in how they calculate variance. This is important to consider when switching between the two libraries.

```python
# Variance in pandas
var_pandas = df.var()

# Variance in NumPy
var_numpy = np.var(df.values)
```
