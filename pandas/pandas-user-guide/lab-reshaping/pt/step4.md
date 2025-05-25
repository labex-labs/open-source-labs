# Tabulações Cruzadas

A tabulação cruzada (Cross tabulation) é um método para analisar quantitativamente a relação entre múltiplas variáveis.

```python
# Cross tabulation between row and col
df.pivot_table(index="row", columns="col", fill_value=0, aggfunc="size")
```
