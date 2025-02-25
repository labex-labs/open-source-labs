# Transposition avec plusieurs agrégations

Nous pouvons également effectuer plusieurs agrégations dans la transposition.

```python
# Transposez df avec la moyenne et la somme de val0
df.pivot_table(values="val0", index="row", columns="col", aggfunc=["mean", "sum"])
```
