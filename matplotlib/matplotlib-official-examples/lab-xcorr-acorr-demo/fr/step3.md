# Tracer la corrélation croisée

Nous allons maintenant tracer la corrélation croisée entre les deux tableaux à l'aide de la fonction `xcorr` dans Matplotlib.

```python
fig, ax = plt.subplots()
ax.xcorr(x, y, usevlines=True, maxlags=50, normed=True, lw=2)
ax.grid(True)
plt.show()
```

La fonction `xcorr` prend les paramètres suivants :

- `x` : le premier tableau de données
- `y` : le second tableau de données
- `usevlines` : booléen, indique s'il faut tracer des lignes verticales allant de 0 à la valeur de corrélation
- `maxlags` : entier, le nombre maximum de retards pour lesquels calculer la corrélation
- `normed` : booléen, indique s'il faut normaliser les valeurs de corrélation
- `lw` : entier, la largeur de la ligne pour le tracé
