# Laden der Bilddaten

Wir verwenden ein Beispiel für Bilddaten namens `bivariate_normal.npy` aus `cbook`, um das ImageGrid zu demonstrieren. Wir laden die Bilddaten mit der Funktion `get_sample_data` aus `cbook`.

```python
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
im1 = Z
im2 = Z[:, :10]
im3 = Z[:, 10:]
vmin, vmax = Z.min(), Z.max()
```
