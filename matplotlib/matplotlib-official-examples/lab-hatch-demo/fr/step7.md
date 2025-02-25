# Ajouter une patch de polygone avec des hachures

Vous pouvez également ajouter une patch de polygone avec des hachures. Dans ce cas, nous allons utiliser la fonction `add_patch` pour ajouter une patch de polygone à notre graphique.

```python
plt.gca().add_patch(Polygon([(10, 20), (30, 50), (50, 10)], hatch='\\/...', facecolor='g'))
```
