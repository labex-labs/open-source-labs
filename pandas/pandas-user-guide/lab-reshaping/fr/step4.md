# Tabulations croisées

La tabulation croisée est une méthode pour analyser quantitativement la relation entre plusieurs variables.

```python
# Tabulation croisée entre row et col
df.pivot_table(index="row", columns="col", fill_value=0, aggfunc="size")
```
