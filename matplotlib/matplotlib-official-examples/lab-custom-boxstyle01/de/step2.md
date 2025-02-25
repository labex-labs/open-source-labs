# Implementieren eines benutzerdefinierten Box-Stils als Klasse

Benutzerdefinierte Box-Stile können auch als Klassen implementiert werden, die `__call__` implementieren. Die Klassen können dann in das `BoxStyle._style_list`-Dict registriert werden, was es ermöglicht, den Box-Stil als Zeichenfolge anzugeben, `bbox=dict(boxstyle="registrierter_name,param=value,...",...)`.

```python
class MyStyle:
    """Eine einfache Box."""

    def __init__(self, pad=0.3):
        """
        Die Argumente müssen Fließkommazahlen sein und Standardwerte haben.

        Parameter
        ----------
        pad : float
            Padding-Größe
        """
        self.pad = pad
        super().__init__()

    def __call__(self, x0, y0, width, height, mutation_size):
        """
        Gegeben die Position und Größe der Box, gibt den Pfad der Box um sie herum zurück.

        Die Rotation wird automatisch übernommen.

        Parameter
        ----------
        x0, y0, width, height : float
            Box-Position und -Größe.
        mutation_size : float
            Referenzmaßstab für die Mutation, typischerweise die Text-Schriftgröße.
        """
        # Padding
        pad = mutation_size * self.pad
        # Breite und Höhe mit hinzugefügtem Padding
        width = width + 2.*pad
        height = height + 2.*pad
        # Grenze der gepaddeten Box
        x0, y0 = x0 - pad, y0 - pad
        x1, y1 = x0 + width, y0 + height
        # Gebe den neuen Pfad zurück
        return Path([(x0, y0),
                     (x1, y0), (x1, y1), (x0, y1),
                     (x0-pad, (y0+y1)/2.), (x0, y0),
                     (x0, y0)],
                    closed=True)


BoxStyle._style_list["angled"] = MyStyle  # Registriere den benutzerdefinierten Stil.

fig, ax = plt.subplots(figsize=(3, 3))
ax.text(0.5, 0.5, "Test", size=30, va="center", ha="center", rotation=30,
        bbox=dict(boxstyle="angled,pad=0.5", alpha=0.2))

del BoxStyle._style_list["angled"]  # Entregistriere es.

plt.show()
```
