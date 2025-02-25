# Crear un gráfico de barras con múltiples sombreados

También puedes usar múltiples sombreados en tu gráfico de barras. En este caso, usaremos una matriz de sombreados para crear múltiples sombreados en nuestras barras.

```python
plt.bar(x, y1, edgecolor='black', hatch=['--', '+', 'x', '\\'])
plt.bar(x, y2, bottom=y1, edgecolor='black', hatch=['*', 'o', 'O', '.'])
```
