# Définition de la classe ItemProperties

Ensuite, nous définissons une classe `ItemProperties` qui sera utilisée pour définir les propriétés de chaque élément du menu. Nous pouvons définir la taille de police, la couleur de l'étiquette, la couleur d'arrière-plan et la valeur alpha pour chaque élément à l'aide de cette classe.

```python
class ItemProperties:
    def __init__(self, fontsize=14, labelcolor='black', bgcolor='yellow',
                 alpha=1.0):
        self.fontsize = fontsize
        self.labelcolor = labelcolor
        self.bgcolor = bgcolor
        self.alpha = alpha
```
