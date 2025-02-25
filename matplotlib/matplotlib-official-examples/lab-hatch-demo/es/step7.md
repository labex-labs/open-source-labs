# Agregar un parche de polígono con sombreado

También puedes agregar un parche de polígono con sombreado. En este caso, usaremos la función `add_patch` para agregar un parche de polígono a nuestro gráfico.

```python
plt.gca().add_patch(Polygon([(10, 20), (30, 50), (50, 10)], hatch='\\/...', facecolor='g'))
```
