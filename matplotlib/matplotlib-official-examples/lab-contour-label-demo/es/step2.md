# Crea etiquetas de contorno con formatters de nivel personalizados

Ahora crearemos etiquetas de contorno con formatters de nivel personalizados. Esto nos permitirá formatear las etiquetas de una manera específica. En este caso, eliminaremos los ceros finales y agregaremos un signo de porcentaje.

```python
def fmt(x):
    s = f"{x:.1f}"
    if s.endswith("0"):
        s = f"{x:.0f}"
    return rf"{s} \%" if plt.rcParams["text.usetex"] else f"{s} %"

fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, CS.levels, inline=True, fmt=fmt, fontsize=10)
```
