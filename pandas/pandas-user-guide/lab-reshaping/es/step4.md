# Tablas cruzadas

La tabulación cruzada es un método para analizar cuantitativamente la relación entre múltiples variables.

```python
# Tabulación cruzada entre row y col
df.pivot_table(index="row", columns="col", fill_value=0, aggfunc="size")
```
