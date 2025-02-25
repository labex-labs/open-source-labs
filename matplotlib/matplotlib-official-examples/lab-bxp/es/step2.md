# Calcular estadísticas del diagrama de caja

La función `boxplot_stats()` del módulo `matplotlib.cbook` calcula las estadísticas necesarias para el diagrama de caja. Pasamos los datos y las etiquetas como parámetros.

```python
# Compute boxplot stats
stats = cbook.boxplot_stats(data, labels=labels, bootstrap=10000)
```
