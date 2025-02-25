# Créez une sous-classe de figure personnalisée

Créez une sous-classe de figure personnalisée appelée `WatermarkFigure` qui ajoute une filigrane de texte au tracé. Cette classe hérite de la classe `Figure` de Matplotlib.

```python
from matplotlib.figure import Figure

class WatermarkFigure(Figure):
    """Une figure avec une filigrane de texte."""

    def __init__(self, *args, watermark=None, **kwargs):
        super().__init__(*args, **kwargs)

        if watermark is not None:
            bbox = dict(boxstyle='square', lw=3, ec='gray',
                        fc=(0.9, 0.9,.9,.5), alpha=0.5)
            self.text(0.5, 0.5, watermark,
                      ha='center', va='center', rotation=30,
                      fontsize=40, color='gray', alpha=0.5, bbox=bbox)
```
