# Definir la clase ItemProperties

A continuación, definimos una clase `ItemProperties` que se utilizará para establecer las propiedades de cada elemento del menú. Podemos establecer el tamaño de fuente, el color de la etiqueta, el color de fondo y el valor alfa para cada elemento utilizando esta clase.

```python
class ItemProperties:
    def __init__(self, fontsize=14, labelcolor='black', bgcolor='yellow',
                 alpha=1.0):
        self.fontsize = fontsize
        self.labelcolor = labelcolor
        self.bgcolor = bgcolor
        self.alpha = alpha
```
