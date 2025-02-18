# Création des sous-graphiques

Ensuite, nous allons créer deux sous-graphiques (subplots) : l'un pour les valeurs aberrantes (outliers) et l'autre pour la majorité des données. Nous utiliserons `plt.subplots` pour créer les sous-graphiques et définir le paramètre `sharex` sur `True` afin qu'ils partagent le même axe des x.

```python
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
```
