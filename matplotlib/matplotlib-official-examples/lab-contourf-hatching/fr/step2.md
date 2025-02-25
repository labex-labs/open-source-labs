# Création de données

Ensuite, nous allons créer quelques données d'échantillonnage pour tracer. Dans cet exemple, nous allons créer une grille 2D de valeurs x et y et les utiliser pour calculer les valeurs z.

```python
# invent some numbers, turning the x and y arrays into simple
# 2d arrays, which make combining them together easier.
x = np.linspace(-3, 5, 150).reshape(1, -1)
y = np.linspace(-3, 5, 120).reshape(-1, 1)
z = np.cos(x) + np.sin(y)
```
