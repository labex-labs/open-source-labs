# Creando los ejes de texto

En este paso, crearemos un eje en _fig_ que contiene 'matplotlib' como texto.

```python
def create_text_axes(fig, height_px):
    """Crea un eje en *fig* que contiene 'matplotlib' como texto."""
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set_aspect("igual")
    ax.set_axis_off()

    path = TextPath((0, 0), "matplotlib", size=height_px * 0.8,
                    prop=get_font_properties())

    angle = 4.25  # grados
    trans = mtrans.Affine2D().skew_deg(angle, 0)

    patch = PathPatch(path, transform=trans + ax.transData, color=MPL_BLUE,
                      lw=0)
    ax.add_patch(patch)
    ax.autoscale()
```
