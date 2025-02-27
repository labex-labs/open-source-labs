# Créer des cartes de couleurs

Nous allons maintenant créer des cartes de couleurs pour tracer les limites de décision de classe. Nous utiliserons des couleurs claires pour l'arrière-plan et des couleurs vives pour les couleurs des classes.

```python
h = 0.05  # pas dans la grille

# Créer des cartes de couleurs
cmap_light = ListedColormap(["#FFAAAA", "#AAFFAA", "#AAAAFF"])
cmap_bold = ListedColormap(["#FF0000", "#00FF00", "#0000FF"])
```
