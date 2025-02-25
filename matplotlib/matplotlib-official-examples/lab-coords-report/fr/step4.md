# Formater le graphique

Pour rendre notre graphique plus lisible, nous pouvons le formater à l'aide des fonctions de formatage de Matplotlib. Dans cet exemple, nous allons formater les étiquettes de l'axe des y pour afficher les valeurs en millions.

```python
def millions(x):
    return '$%1.1fM' % (x * 1e-6)

ax.fmt_ydata = millions
```
