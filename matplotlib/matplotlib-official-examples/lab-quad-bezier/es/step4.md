# Creando la gráfica

Ahora podemos crear la gráfica agregando el objeto `PathPatch` al eje y dibujando un punto rojo que debería estar sobre la curva. También estableceremos el título de la gráfica en `'Bezier Curve'`.

```python
fig, ax = plt.subplots()

ax.add_patch(bezier_patch)
ax.plot([0.75], [0.25], "ro")
ax.set_title('Bezier Curve')

plt.show()
```

El código final debería verse así:

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.path as mpath

Path = mpath.Path

bezier_path = Path([(0, 0), (1, 0), (1, 1), (0, 0)],
                   [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY])

bezier_patch = mpatches.PathPatch(bezier_path, fc="none")

fig, ax = plt.subplots()

ax.add_patch(bezier_patch)
ax.plot([0.75], [0.25], "ro")
ax.set_title('Bezier Curve')

plt.show()
```
