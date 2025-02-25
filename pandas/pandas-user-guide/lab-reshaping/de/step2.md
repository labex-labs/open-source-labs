# Drehen mit einfachen Aggregationen

Pivot ist eine der wichtigsten Methoden zur Datenumformung in Pandas. Es bietet eine Möglichkeit, Ihre Daten umzuwandeln, sodass Sie sie aus verschiedenen Perspektiven betrachten können.

```python
# Pivot df mit der durchschnittlichen val0
df.pivot_table(values="val0", index="row", columns="col", aggfunc="mean", fill_value=0)
```
