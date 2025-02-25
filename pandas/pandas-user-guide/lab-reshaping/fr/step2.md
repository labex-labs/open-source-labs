# Transposition avec des agrégations simples

La transposition est l'une des méthodes clés pour restructurer les données dans Pandas. Elle fournit un moyen de transformer vos données afin que vous puissiez les visualiser sous différents angles.

```python
# Transposez df avec la moyenne de val0
df.pivot_table(values="val0", index="row", columns="col", aggfunc="mean", fill_value=0)
```
