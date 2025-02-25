# Ajouter des lignes à la Figure

Nous pouvons ajouter des lignes à la figure à l'aide de la méthode `fig.add_artist()`. Nous allons créer deux lignes - l'une allant de (0,0) à (1,1) et l'autre de (0,1) à (1,0).

```python
fig.add_artist(lines.Line2D([0, 1], [0, 1]))
fig.add_artist(lines.Line2D([0, 1], [1, 0]))
```
