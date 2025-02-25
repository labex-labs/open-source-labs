# Crear un esquema de colores

Crearemos un esquema de colores para la tabla usando la función `plt.cm.BuPu`. Usaremos una tonalidad pastelería de azul y morado para las filas.

```python
colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
```
