# Ajout de MultiCursor

Enfin, nous allons ajouter la fonction `MultiCursor` pour afficher un curseur sur les trois graphiques lorsqu'on survole un point de données.

```python
multi = MultiCursor(None, (ax1, ax2, ax3), color='r', lw=1)
plt.show()
```
