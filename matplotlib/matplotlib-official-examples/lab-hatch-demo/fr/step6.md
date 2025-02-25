# Ajouter une patch d'ellipse avec des hachures

Vous pouvez également ajouter des patches hachurées à votre graphique. Dans ce cas, nous allons utiliser la fonction `add_patch` pour ajouter une patch d'ellipse à notre graphique.

```python
plt.gca().add_patch(Ellipse((4, 50), 10, 10, fill=True, hatch='*', facecolor='y'))
```
