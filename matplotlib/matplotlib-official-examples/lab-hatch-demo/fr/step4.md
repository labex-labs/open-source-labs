# Créer un graphique en barres avec plusieurs hachures

Vous pouvez également utiliser plusieurs hachures dans votre graphique en barres. Dans ce cas, nous allons utiliser un tableau d'hachures pour créer plusieurs hachures sur nos barres.

```python
plt.bar(x, y1, edgecolor='black', hatch=['--', '+', 'x', '\\'])
plt.bar(x, y2, bottom=y1, edgecolor='black', hatch=['*', 'o', 'O', '.'])
```
