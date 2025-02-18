# Définition des limites de l'axe des y

Nous allons limiter l'axe des y du premier sous-graphique pour n'afficher que les valeurs aberrantes (outliers) et celui du deuxième sous-graphique pour afficher la majorité des données. Nous utiliserons `ax1.set_ylim` et `ax2.set_ylim` pour définir les limites de l'axe des y.

```python
ax1.set_ylim(.78, 1.)  # outliers only
ax2.set_ylim(0,.22)  # most of the data
```
