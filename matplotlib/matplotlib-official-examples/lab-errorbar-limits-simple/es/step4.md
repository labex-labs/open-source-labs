# Crear la gráfica de barras de error con solo límites superiores

En este paso, creamos una gráfica de barras de error con solo límites superiores.

```python
plt.errorbar(x, y + 2, yerr=yerr, uplims=True, label='uplims=True')
```
