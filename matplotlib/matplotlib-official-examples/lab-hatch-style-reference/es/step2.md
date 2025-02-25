# Crear la función hatches_plot

La función hatches_plot creará un rectángulo con el patrón de sombreado especificado y lo agregará al eje. También agregará un texto con el patrón de sombreado.

```python
def hatches_plot(ax, h):
    ax.add_patch(Rectangle((0, 0), 2, 2, fill=False, hatch=h))
    ax.text(1, -0.5, f"' {h} '", size=15, ha="center")
    ax.axis('equal')
    ax.axis('off')
```
