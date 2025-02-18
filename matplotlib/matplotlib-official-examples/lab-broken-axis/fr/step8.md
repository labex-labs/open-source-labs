# Création des lignes obliques de découpe

Enfin, nous allons créer les lignes obliques de découpe. Nous allons créer des objets de ligne dans les coordonnées des axes et utiliser `ax1.transAxes` et `ax2.transAxes` pour les transformer dans les coordonnées de chaque sous-graphique. Nous utiliserons `ax1.plot` et `ax2.plot` pour tracer les lignes. Nous utiliserons également `marker` pour spécifier le style du marqueur, `markersize` pour définir la taille des marqueurs, `linestyle` pour définir le style de la ligne, `color` pour définir la couleur de la ligne, `mec` pour définir la couleur du bord du marqueur et `mew` pour définir la largeur du bord du marqueur.

```python
d =.5
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)
```
