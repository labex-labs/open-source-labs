# Créez une figure et un ImageGrid

Ensuite, nous créons une figure et un ImageGrid avec le paramètre `nrows_ncols` pour définir le nombre de lignes et de colonnes de la grille.

```python
fig = plt.figure(figsize=(5.5, 3.5))
grid = ImageGrid(fig, 111,  # similaire à subplot(111)
                 nrows_ncols=(1, 3),
                 axes_pad=0.1,
                 label_mode="L")
```
