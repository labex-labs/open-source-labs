# Ombré plat, grille de même forme

Si la grille est de la même forme que les données dans chaque dimension, nous ne pouvons pas utiliser `shading='flat'`. Historique : Matplotlib supprimait silencieusement la dernière ligne et la dernière colonne de `Z` dans ce cas, pour correspondre au comportement de Matlab. Si ce comportement est toujours souhaité, supprimez simplement la dernière ligne et la dernière colonne manuellement. Nous pouvons visualiser la grille à l'aide du bloc de code suivant :

```python
fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z[:-1, :-1], shading='flat', cmap='viridis')
ax.set_title('Flat Shading, Same Shape Grid')
plt.show()
```
