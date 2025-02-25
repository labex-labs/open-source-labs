# Ombrer les régions

Nous allons utiliser `fill_between` pour ombrer les régions au-dessus et au-dessous de la ligne horizontale où l'onde sinusoïdale est positive et négative respectivement.

```python
ax.fill_between(t, 1, where=s > 0, facecolor='green', alpha=.5)
ax.fill_between(t, -1, where=s < 0, facecolor='red', alpha=.5)
```
