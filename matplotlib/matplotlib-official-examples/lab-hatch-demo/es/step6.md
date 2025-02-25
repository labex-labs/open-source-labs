# Agregar un parche de elipse con sombreado

También puedes agregar parches sombreados a tu gráfico. En este caso, usaremos la función `add_patch` para agregar un parche de elipse a nuestro gráfico.

```python
plt.gca().add_patch(Ellipse((4, 50), 10, 10, fill=True, hatch='*', facecolor='y'))
```
