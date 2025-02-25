# Définir les données d'image

Nous définissons une fonction qui renvoie des données d'image d'échantillonnage et son étendue.

```python
def get_demo_image():
    z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 array
    return z, (-3, 4, -4, 3)
```
