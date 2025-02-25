# Crear un gráfico de barras con sombreado

Ahora que tienes tus datos, puedes crear un gráfico de barras con sombreado. Puedes usar el sombreado para crear patrones en las barras de tu gráfico. En este caso, usaremos el parámetro `hatch` para agregar sombreado a nuestras barras.

```python
plt.bar(x, y1, edgecolor='black', hatch="/")
plt.bar(x, y2, bottom=y1, edgecolor='black', hatch='//')
```
