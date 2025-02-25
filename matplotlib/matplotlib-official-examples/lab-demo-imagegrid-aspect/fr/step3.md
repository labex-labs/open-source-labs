# Créez les ImageGrids

Nous allons créer deux ImageGrids pour afficher nos images. Le premier ImageGrid aura deux lignes et deux colonnes, et le second ImageGrid aura également deux lignes et deux colonnes.

```python
grid1 = ImageGrid(fig, 121, (2, 2), axes_pad=0.1, aspect=True, share_all=True)
grid2 = ImageGrid(fig, 122, (2, 2), axes_pad=0.1, aspect=True, share_all=True)
```
