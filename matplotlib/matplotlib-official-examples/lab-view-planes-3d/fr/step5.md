# Créez le graphique 3D

Nous utilisons `subplot_mosaic` pour créer le graphique 3D sur la base de la disposition définie dans l'étape 4.

```python
fig, axd = plt.subplot_mosaic(layout, subplot_kw={'projection': '3d'},
                              figsize=(12, 8.5))
```
