# Crear la gráfica de barras de error con subconjuntos de límites superiores e inferiores

En este paso, creamos una gráfica de barras de error con subconjuntos de límites superiores e inferiores.

```python
upperlimits = [True, False] * 5
lowerlimits = [False, True] * 5
plt.errorbar(x, y, yerr=yerr, uplims=upperlimits, lolims=lowerlimits, label='subsets of uplims and lolims')
```
