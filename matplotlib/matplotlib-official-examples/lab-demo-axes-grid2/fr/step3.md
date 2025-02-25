# Préparez les données d'échantillonnage

Nous utiliserons la fonction `get_sample_data` de cbook pour obtenir des données d'échantillonnage. Nous préparerons ensuite les images à afficher dans la grille.

```python
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
extent = (-3, 4, -4, 3)
ZS = [Z[i::3, :] for i in range(3)]
extent = extent[0], extent[1]/3., extent[2], extent[3]
```
