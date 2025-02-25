# Ombré de Gouraud

On peut également spécifier l'`ombrage de Gouraud`, où la couleur dans les quadrilatères est interpolée linéairement entre les points de la grille. Les formes de `X`, `Y` et `Z` doivent être les mêmes. Nous pouvons visualiser la grille à l'aide du bloc de code suivant :

```python
fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z, shading='gouraud', cmap='viridis')
ax.set_title('Gouraud Shading')
plt.show()
```
