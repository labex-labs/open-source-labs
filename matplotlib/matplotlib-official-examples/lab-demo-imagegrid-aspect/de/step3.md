# Erstellen der ImageGrids

Wir werden zwei ImageGrids erstellen, um unsere Bilder anzuzeigen. Das erste ImageGrid wird zwei Zeilen und zwei Spalten haben, und das zweite ImageGrid wird ebenfalls zwei Zeilen und zwei Spalten haben.

```python
grid1 = ImageGrid(fig, 121, (2, 2), axes_pad=0.1, aspect=True, share_all=True)
grid2 = ImageGrid(fig, 122, (2, 2), axes_pad=0.1, aspect=True, share_all=True)
```
