# Créer le patch

Pour créer le patch, nous allons utiliser le module `patches` de Matplotlib. Nous allons créer un patch circulaire avec un rayon de 200 pixels, centré sur le point (260, 200).

```python
patch = patches.Circle((260, 200), radius=200, transform=ax.transData)
```
