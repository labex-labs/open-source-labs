# Demo 1 - Farbskala an jeder Achse

Wir werden mit dem folgenden Code ein Gitter von 3 Bildern mit einer Farbskala an jeder Achse erstellen:

```python
grid = ImageGrid(
    fig, 211, nrows_ncols=(1, 3), axes_pad=0.05, label_mode="1", share_all=True,
    cbar_location="top", cbar_mode="each", cbar_size="7%", cbar_pad="1%")
grid[0].set(xticks=[-2, 0], yticks=[-2, 0, 2])

for i, (ax, z) in enumerate(zip(grid, ZS)):
    im = ax.imshow(z, origin="lower", extent=extent)
    cb = ax.cax.colorbar(im)
    # Ändern der Farbskala-Ticks
    if i in [1, 2]:
        cb.set_ticks([-1, 0, 1])

for ax, im_title in zip(grid, ["Bild 1", "Bild 2", "Bild 3"]):
    add_inner_title(ax, im_title, loc='lower left')
```

- Wir erstellen ein Gitter von 3 Bildern mit `ImageGrid`.
- Wir setzen den `cbar_mode` auf "each", um an jeder Achse eine Farbskala hinzuzufügen.
- Wir setzen den Parameter `share_all` auf True, um die x- und y-Achsen über alle Bilder hinweg zu teilen.
- Wir setzen den Parameter `cbar_location` auf "top", um die Farbskalen oben zu positionieren.
- Wir setzen die `xticks` und `yticks` für das erste Bild.
- Wir durchlaufen jedes Bild und fügen das Bild zur Achse hinzu, indem wir `imshow` verwenden.
- Wir fügen jeder Achse eine Farbskala hinzu, indem wir `ax.cax.colorbar` verwenden.
- Wir setzen die Farbskala-Ticks für das zweite und dritte Bild.
- Wir fügen jedem Bild einen Titel hinzu, indem wir `add_inner_title` verwenden.
