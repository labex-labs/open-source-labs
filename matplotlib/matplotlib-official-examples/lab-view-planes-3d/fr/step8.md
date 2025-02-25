# Personnalisez les étiquettes d'échelonnement et les étiquettes d'axe pour chaque plan de vue principale 3D

Nous personnalisons les étiquettes d'échelonnement et les étiquettes d'axe pour chaque plan de vue principale 3D pour supprimer toute étiquette inutile.

```python
for plane in ('XY', '-XY'):
    axd[plane].set_zticklabels([])
    axd[plane].set_zlabel('')
for plane in ('XZ', '-XZ'):
    axd[plane].set_yticklabels([])
    axd[plane].set_ylabel('')
for plane in ('YZ', '-YZ'):
    axd[plane].set_xticklabels([])
    axd[plane].set_xlabel('')
```
