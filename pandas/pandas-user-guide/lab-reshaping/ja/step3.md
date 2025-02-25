# 複数の集約を伴うピボット

ピボットでは、複数の集約も行うことができます。

```python
# Pivot df with the mean and sum of val0
df.pivot_table(values="val0", index="row", columns="col", aggfunc=["mean", "sum"])
```
