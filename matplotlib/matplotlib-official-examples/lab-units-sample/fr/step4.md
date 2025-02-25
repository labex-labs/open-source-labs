# Créez le graphique

Créez une grille de sous-graphiques 2x2 à l'aide de la fonction `subplots`. Ensuite, utilisez la fonction `plot` pour tracer les données sur chaque sous-graphique.

```python
fig, axs = plt.subplots(2, 2, layout='constrained')

axs[0, 0].plot(cms, cms)

axs[0, 1].plot(cms, cms, xunits=cm, yunits=inch)

axs[1, 0].plot(cms, cms, xunits=inch, yunits=cm)
axs[1, 0].set_xlim(-1, 4)  # Les scalaires sont interprétés dans les unités actuelles

axs[1, 1].plot(cms, cms, xunits=inch, yunits=inch)
axs[1, 1].set_xlim(3*cm, 6*cm)  # Les cm sont convertis en pouces
```
