# Pivoteamento com Múltiplas Agregações

Também podemos realizar múltiplas agregações no Pivot.

```python
# Pivot df with the mean and sum of val0
df.pivot_table(values="val0", index="row", columns="col", aggfunc=["mean", "sum"])
```
