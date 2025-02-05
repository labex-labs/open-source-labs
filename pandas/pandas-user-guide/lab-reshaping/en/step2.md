# Pivoting with Single Aggregations

Pivot is one of the key methods for reshaping data in Pandas. It provides a way to transform your data so that you can view it from different angles.

```python
# Pivot df with the mean of val0
df.pivot_table(values="val0", index="row", columns="col", aggfunc="mean", fill_value=0)
```
