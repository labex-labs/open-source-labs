# Ombré par valeur la plus proche, grille de même forme

Généralement, supprimer une ligne et une colonne de données n'est pas ce que l'utilisateur veut lorsqu'ils rendent `X`, `Y` et `Z` toutes de la même forme. Dans ce cas, Matplotlib autorise `shading='nearest'` et centre les quadrilatères colorés sur les points de la grille. Si une grille de forme incorrecte est passée avec `shading='nearest'`, une erreur est levée. Nous pouvons visualiser la grille à l'aide du bloc de code suivant :

```python
fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z, shading='nearest', cmap='viridis')
ax.set_title('Nearest Shading, Same Shape Grid')
plt.show()
```
