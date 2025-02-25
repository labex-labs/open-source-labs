# Créez une flèche simple

Maintenant, nous allons créer une flèche de direction ancrée simple à l'aide de la classe `AnchoredDirectionArrows`. Cette flèche indiquera les directions X et Y dans le graphique.

```python
# Simple example
simple_arrow = AnchoredDirectionArrows(ax.transAxes, 'X', 'Y')
ax.add_artist(simple_arrow)
```
