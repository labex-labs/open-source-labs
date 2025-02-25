# Ombré plat

La fonction `pcolormesh` de Matplotlib peut visualiser des grilles 2D. La spécification de grille avec les hypothèses les moins nombreuses est `shading='flat'` et si la grille est d'une dimension supérieure à la donnée dans chaque dimension, c'est-à-dire a une forme `(M+1, N+1)`. Dans ce cas, `X` et `Y` spécifient les coins des quadrilatères qui sont colorés avec les valeurs de `Z`. Nous pouvons visualiser la grille à l'aide du bloc de code suivant :

```python
fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z, shading='flat', cmap='viridis')
ax.set_title('Flat Shading')
plt.show()
```
