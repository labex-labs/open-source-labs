# Definir a classe ItemProperties

Em seguida, definimos uma classe `ItemProperties` que será usada para definir as propriedades de cada item do menu. Podemos definir o tamanho da fonte, a cor do rótulo, a cor de fundo e o valor alfa para cada item usando esta classe.

```python
class ItemProperties:
    def __init__(self, fontsize=14, labelcolor='black', bgcolor='yellow',
                 alpha=1.0):
        self.fontsize = fontsize
        self.labelcolor = labelcolor
        self.bgcolor = bgcolor
        self.alpha = alpha
```
