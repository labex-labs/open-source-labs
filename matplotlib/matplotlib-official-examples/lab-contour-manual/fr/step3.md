# Créez le tracé

L'étape suivante est de créer le tracé. Cela peut être fait à l'aide de la fonction ContourSet.

```python
fig, ax = plt.subplots()

# Contours remplis en utilisant filled=True.
cs = ContourSet(ax, [0, 1, 2], [filled01, filled12], filled=True, cmap=cm.bone)
cbar = fig.colorbar(cs)

# Lignes de niveau (non-remplies).
lines = ContourSet(
    ax, [0, 1, 2], [lines0, lines1, lines2], cmap=cm.cool, linewidths=3)
cbar.add_lines(lines)

ax.set(xlim=(-0.5, 3.5), ylim=(-0.5, 4.5),
       title='Contours spécifiés par l\'utilisateur')
```
