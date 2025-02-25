# Demo 2 - Geteilte Farbskala

Wir werden mit dem folgenden Code ein Gitter von 3 Bildern mit einer geteilten Farbskala erstellen:

```python
grid2 = ImageGrid(
    fig, 212, nrows_ncols=(1, 3), axes_pad=0.05, label_mode="1", share_all=True,
    cbar_location="right", cbar_mode="single", cbar_size="10%", cbar_pad=0.05)
grid2[0].set(xlabel="X", ylabel="Y", xticks=[-2, 0], yticks=[-2, 0, 2])

clim = (np.min(ZS), np.max(ZS))
for ax, z in zip(grid2, ZS):
    im = ax.imshow(z, clim=clim, origin="lower", extent=extent)

# Mit cbar_mode="single" sind die cax-Attribute aller Achsen identisch.
ax.cax.colorbar(im)

for ax, im_title in zip(grid2, ["(a)", "(b)", "(c)"]):
    add_inner_title(ax, im_title, loc='upper left')
```

- Wir erstellen ein Gitter von 3 Bildern mit `ImageGrid`.
- Wir setzen den `cbar_mode` auf "single", um eine geteilte Farbskala hinzuzufügen.
- Wir setzen den Parameter `share_all` auf True, um die x- und y-Achsen über alle Bilder hinweg zu teilen.
- Wir setzen den Parameter `cbar_location` auf "right", um die Farbskala rechts zu positionieren.
- Wir setzen die `xticks` und `yticks` für das erste Bild.
- Wir durchlaufen jedes Bild und fügen das Bild zur Achse hinzu, indem wir `imshow` verwenden.
- Wir setzen den Parameter `clim`, um sicherzustellen, dass alle Bilder die gleiche Farbskala verwenden.
- Wir fügen einer geteilten Farbskala zur Achse hinzu, indem wir `ax.cax.colorbar` verwenden.
- Wir fügen jedem Bild einen Titel hinzu, indem wir `add_inner_title` verwenden.
