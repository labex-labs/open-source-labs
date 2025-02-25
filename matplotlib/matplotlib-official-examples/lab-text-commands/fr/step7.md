# Ajout d'annotations au graphique

Nous pouvons ajouter des annotations au graphique à l'aide de la fonction `ax.annotate()`. Cette fonction prend trois arguments : le texte de l'annotation, les coordonnées xy du point à annoter et les coordonnées xy de la position du texte. Nous pouvons personnaliser le style de l'annotation à l'aide de l'argument `arrowprops`.

```python
ax.annotate('annotate', xy=(2, 1), xytext=(3, 4),
            arrowprops=dict(facecolor='black', shrink=0.05))
```
