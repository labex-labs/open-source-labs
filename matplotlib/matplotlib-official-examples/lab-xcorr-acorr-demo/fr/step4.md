# Tracer l'auto - corrélation

Nous allons maintenant tracer l'auto - corrélation du tableau `x` à l'aide de la fonction `acorr` dans Matplotlib.

```python
fig, ax = plt.subplots()
ax.acorr(x, usevlines=True, normed=True, maxlags=50, lw=2)
ax.grid(True)
plt.show()
```

La fonction `acorr` prend les paramètres suivants :

- `x` : le tableau de données pour lequel calculer l'auto - corrélation
- `usevlines` : booléen, indique s'il faut tracer des lignes verticales allant de 0 à la valeur de corrélation
- `normed` : booléen, indique s'il faut normaliser les valeurs de corrélation
- `maxlags` : entier, le nombre maximum de retards pour lesquels calculer la corrélation
- `lw` : entier, la largeur de la ligne pour le tracé
