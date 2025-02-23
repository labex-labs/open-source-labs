# Définissez la fonction de rappel de dessin

Nous allons définir une fonction qui sera appelée chaque fois que le graphique est dessiné. Cette fonction calculera les boîtes englobantes des étiquettes de l'axe des ordonnées, déterminera si le sous-graphique laisse suffisamment de place pour les étiquettes et ajustera les paramètres du sous-graphique si nécessaire.

```python
def on_draw(event):
    bboxes = []
    for label in ax.get_yticklabels():
        # Boîte englobante en pixels
        bbox_px = label.get_window_extent()
        # Transformer en coordonnées relatives de la figure. Ceci est l'inverse de
        # transFigure.
        bbox_fig = bbox_px.transformed(fig.transFigure.inverted())
        bboxes.append(bbox_fig)
    # la boîte englobante qui englobe toutes les boîtes englobantes, encore en coordonnées relatives de la figure
    bbox = mtransforms.Bbox.union(bboxes)
    if fig.subplotpars.left < bbox.width:
        # Décaler le bord gauche du sous-graphique plus à droite
        fig.subplots_adjust(left=1.1*bbox.width)  # ajouter un peu d'espace
        fig.canvas.draw()
```
