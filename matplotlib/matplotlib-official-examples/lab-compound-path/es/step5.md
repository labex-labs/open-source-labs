# Creando la gráfica

Crearemos la gráfica y agregaremos el `PathPatch` a la gráfica. Estableceremos el título de la gráfica en `'A Compound Path'`.

```python
fig, ax = plt.subplots()
ax.add_patch(pathpatch)
ax.set_title('A Compound Path')

ax.autoscale_view()

plt.show()
```
