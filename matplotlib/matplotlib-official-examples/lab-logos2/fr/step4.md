# Création des axes de texte

Dans cette étape, nous allons créer un axe dans _fig_ qui contient'matplotlib' sous forme de texte.

```python
def create_text_axes(fig, height_px):
    """Crée un Axe dans *fig* qui contient'matplotlib' sous forme de Texte."""
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set_aspect("égal")
    ax.set_axis_off()

    path = TextPath((0, 0), "matplotlib", size=height_px * 0.8,
                    prop=get_font_properties())

    angle = 4.25  # degrés
    trans = mtrans.Affine2D().skew_deg(angle, 0)

    patch = PathPatch(path, transform=trans + ax.transData, color=MPL_BLUE,
                      lw=0)
    ax.add_patch(patch)
    ax.autoscale()
```
