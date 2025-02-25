# Configurar el rectángulo

Definiremos la posición y las dimensiones del rectángulo utilizando las variables `left`, `bottom`, `width` y `height`. Luego, crearemos el rectángulo utilizando la clase `Rectangle` y lo agregaremos a la gráfica utilizando el método `add_patch`.

```python
left, bottom, width, height = (-1, -1, 2, 2)
rect = plt.Rectangle((left, bottom), width, height,
                     facecolor="black", alpha=0.1)

fig, ax = plt.subplots()
ax.add_patch(rect)
```
