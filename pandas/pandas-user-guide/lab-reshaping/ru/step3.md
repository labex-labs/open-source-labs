# Переворачивание с помощью нескольких агрегаций

Мы также можем выполнять несколько агрегаций при использовании метода Pivot.

```python
# Pivot df with the mean and sum of val0
df.pivot_table(values="val0", index="row", columns="col", aggfunc=["mean", "sum"])
```
