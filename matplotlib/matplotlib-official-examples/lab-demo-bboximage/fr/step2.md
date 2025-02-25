# Créez une BboxImage avec du texte

Nous commençons par créer une BboxImage avec du texte. Nous créons un objet `text` avec la méthode `text()` et l'ajoutons à l'objet `ax1`. Nous créons ensuite un objet `BboxImage` en utilisant la méthode `add_artist()`. Nous passons la méthode `get_window_extent` de l'objet `text` au constructeur `BboxImage` pour obtenir la boîte englobante du texte. Nous passons également un tableau 1D de forme (1, 256) au paramètre `data` du constructeur `BboxImage` pour créer une image.

```python
fig, (ax1, ax2) = plt.subplots(ncols=2)

txt = ax1.text(0.5, 0.5, "test", size=30, ha="center", color="w")
ax1.add_artist(
    BboxImage(txt.get_window_extent, data=np.arange(256).reshape((1, -1))))
```
