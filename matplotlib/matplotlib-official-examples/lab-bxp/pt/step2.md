# Calcular as estatísticas do boxplot

A função `boxplot_stats()` do módulo `matplotlib.cbook` calcula as estatísticas necessárias para o boxplot. Passamos os dados e os rótulos como parâmetros.

```python
# Compute boxplot stats
stats = cbook.boxplot_stats(data, labels=labels, bootstrap=10000)
```
