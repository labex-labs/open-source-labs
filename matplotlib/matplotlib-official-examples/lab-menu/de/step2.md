# Definiere die ItemProperties-Klasse

Als nächstes definieren wir eine `ItemProperties`-Klasse, die verwendet werden soll, um die Eigenschaften für jedes Menüelement festzulegen. Mit dieser Klasse können wir die Schriftgröße, die Label-Farbe, die Hintergrundfarbe und den Alpha-Wert für jedes Element festlegen.

```python
class ItemProperties:
    def __init__(self, fontsize=14, labelcolor='black', bgcolor='yellow',
                 alpha=1.0):
        self.fontsize = fontsize
        self.labelcolor = labelcolor
        self.bgcolor = bgcolor
        self.alpha = alpha
```
