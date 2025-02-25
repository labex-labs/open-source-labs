# Crear la gráfica de barras de error con ambos límites (predeterminado)

En este paso, creamos una gráfica de barras de error con límites superior e inferior, que es el comportamiento predeterminado.

```python
plt.errorbar(x, y + 3, yerr=yerr, label='both limits (default)')
```
