# Remplissage des diagrammes en boîte avec des couleurs personnalisées

Ensuite, nous allons remplir les diagrammes en boîte avec des couleurs personnalisées. Nous allons créer une liste de couleurs et utiliser une boucle pour remplir chaque boîte avec une couleur différente.

```python
colors = ['pink', 'lightblue', 'lightgreen']
for bplot in (bplot1, bplot2):
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)
```
