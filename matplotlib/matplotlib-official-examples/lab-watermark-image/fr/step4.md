# Superposer une image

Pour superposer l'image sur le graphique, nous pouvons utiliser la méthode `figimage` de la classe `matplotlib.figure.Figure`. Nous devons spécifier l'image, la position de l'image sur le graphique, l'ordre z (pour déplacer l'image vers l'avant) et l'alpha (pour rendre l'image semi-transparente).

```python
fig.figimage(im, 25, 25, zorder=3, alpha=.7)
```
