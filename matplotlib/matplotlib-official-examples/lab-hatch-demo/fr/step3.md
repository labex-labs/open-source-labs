# Créer un graphique en barres avec des hachures

Maintenant que vous avez vos données, vous pouvez créer un graphique en barres avec des hachures. Vous pouvez utiliser les hachures pour créer des motifs sur les barres de votre graphique. Dans ce cas, nous allons utiliser le paramètre `hatch` pour ajouter des hachures à nos barres.

```python
plt.bar(x, y1, edgecolor='black', hatch="/")
plt.bar(x, y2, bottom=y1, edgecolor='black', hatch='//')
```
