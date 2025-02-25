# Supprimez les points

Nous allons supprimer les points où y > 0,7. Nous allons créer un nouveau tableau x et un tableau y ne contenant que les points restants.

```python
x2 = x[y <= 0.7]
y2 = y[y <= 0.7]
```
