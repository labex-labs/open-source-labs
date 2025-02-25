# Crear la gráfica de barras de error con límites superiores e inferiores

En este paso, creamos una gráfica de barras de error con límites superiores e inferiores.

```python
plt.errorbar(x, y + 1, yerr=yerr, uplims=True, lolims=True, label='uplims=True, lolims=True')
```
