# Resaltando intervalos de un eje con `axhspan` y `axvspan`

Otra forma útil de utilizar regiones rellenas es para resaltar intervalos horizontales o verticales de un eje. Para eso, Matplotlib tiene las funciones auxiliares `axhspan` y `axvspan`. Consulte la galería `axhspan_demo` para obtener más información.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.axhspan(0.25, 0.75, facecolor='0.5', alpha=0.5)
ax.axvspan(6, 7, facecolor='r', alpha=0.5)

plt.show()
```
