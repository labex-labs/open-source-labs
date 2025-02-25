# Pivotamiento con múltiples agregaciones

También podemos realizar múltiples agregaciones en Pivot.

```python
# Pivot df con la media y la suma de val0
df.pivot_table(values="val0", index="row", columns="col", aggfunc=["mean", "sum"])
```
