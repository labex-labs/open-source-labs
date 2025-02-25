# Drehen mit mehreren Aggregationen

Wir können auch mehrere Aggregationen in Pivot durchführen.

```python
# Pivot df mit der durchschnittlichen und der Summe von val0
df.pivot_table(values="val0", index="row", columns="col", aggfunc=["mean", "sum"])
```
