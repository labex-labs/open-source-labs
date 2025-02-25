# Crear la gráfica

Necesitamos crear la gráfica y agregar el polígono a ella.

```python
fig, ax = plt.subplots()
ax.add_patch(poly)
p = PolygonInteractor(ax, poly)

ax.set_title('Haga clic y arrastre un punto para moverlo')
ax.set_xlim((-2, 2))
ax.set_ylim((-2, 2))
plt.show()
```
