# Создание осей для текста

В этом шаге мы создадим ось в _fig_, которая содержит слово 'matplotlib' в виде текста.

```python
def create_text_axes(fig, height_px):
    """Создаёт ось в *fig*, которая содержит слово 'matplotlib' в виде текста."""
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set_aspect("equal")
    ax.set_axis_off()

    path = TextPath((0, 0), "matplotlib", size=height_px * 0.8,
                    prop=get_font_properties())

    angle = 4.25  # градусы
    trans = mtrans.Affine2D().skew_deg(angle, 0)

    patch = PathPatch(path, transform=trans + ax.transData, color=MPL_BLUE,
                      lw=0)
    ax.add_patch(patch)
    ax.autoscale()
```
