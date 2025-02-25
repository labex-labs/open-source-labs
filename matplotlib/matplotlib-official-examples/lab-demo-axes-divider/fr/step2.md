# Obtenir une image de démonstration

Dans cette étape, nous allons définir une fonction pour obtenir une image de démonstration et son étendue. Nous utiliserons la fonction `get_sample_data()` de `cbook` pour obtenir une image d'échantillonnage.

```python
def get_demo_image():
    z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 array
    return z, (-3, 4, -4, 3)
```
