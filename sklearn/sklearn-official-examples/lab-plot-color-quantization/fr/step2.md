# Convertir l'image en flottants et redimensionner

Nous allons convertir l'image en flottants et la redimensionner en un tableau numpy 2D afin qu'elle puisse être traitée par l'algorithme K-Means.

```python
# Convertir en flottants au lieu du codage entier par défaut de 8 bits.
china = np.array(china, dtype=np.float64) / 255

# Obtenir les dimensions de l'image
w, h, d = original_shape = tuple(china.shape)
assert d == 3

# Redimensionner l'image en un tableau numpy 2D
image_array = np.reshape(china, (w * h, d))
```
