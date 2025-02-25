# Das Kontur-Bild erstellen

In diesem Schritt erstellst du das Kontur-Bild, indem du die `contour`- und `contourf`-Funktionen von Matplotlib verwendest.

```python
# Erhöhe die obere Grenze, um Abbruchfehler zu vermeiden.
levels = np.arange(-2.0, 1.601, 0.4)

norm = cm.colors.Normalize(vmax=abs(Z).max(), vmin=-abs(Z).max())
cmap = cm.PRGn

fig, _axs = plt.subplots(nrows=2, ncols=2)
fig.subplots_adjust(hspace=0.3)
axs = _axs.flatten()

cset1 = axs[0].contourf(X, Y, Z, levels, norm=norm,
                        cmap=cmap.resampled(len(levels) - 1))
# Dies ist nicht erforderlich, aber für die Farbkarte benötigen wir nur
# die Anzahl der Ebenen minus 1. Um Diskretisierungsfehler zu vermeiden,
# verwenden wir diese Zahl oder eine große Zahl wie die Standardzahl (256).

# Wenn wir sowohl Linien als auch gefüllte Bereiche möchten, müssen wir
# `contour` separat aufrufen; versuchen Sie nicht, die Kantenfarbe oder
# die Kantenbreite der Polygone in den von `contourf` zurückgegebenen
# Sammlungen zu ändern.
# Verwenden Sie die von der vorherigen Funktion zurückgegebenen Ebenen,
# um sicherzustellen, dass sie die gleichen sind.

cset2 = axs[0].contour(X, Y, Z, cset1.levels, colors='k')

# Wir brauchen eigentlich keine durchgezogenen Konturlinien, um negative
# Bereiche anzuzeigen, also schalten wir sie aus.

for c in cset2.collections:
    c.set_linestyle('solid')

# Hier ist es einfacher, eine separate `contour`-Funktion aufzurufen,
# als ein Array von Farben und Linienbreiten einzurichten.
# Wir erstellen eine dicke grüne Linie als Null-Kontur.
# Geben Sie die Null-Ebene als Tupel an, das nur 0 enthält.

cset3 = axs[0].contour(X, Y, Z, (0,), colors='g', linewidths=2)
axs[0].set_title('Gefüllte Konturen')
fig.colorbar(cset1, ax=axs[0])


axs[1].imshow(Z, extent=extent, cmap=cmap, norm=norm)
axs[1].contour(Z, levels, colors='k', origin='upper', extent=extent)
axs[1].set_title("Bild, Ursprung 'upper'")

axs[2].imshow(Z, origin='lower', extent=extent, cmap=cmap, norm=norm)
axs[2].contour(Z, levels, colors='k', origin='lower', extent=extent)
axs[2].set_title("Bild, Ursprung 'lower'")

# Wir verwenden hier die Interpolation "nearest", um die tatsächlichen
# Bildpixel anzuzeigen.
# Beachten Sie, dass die Konturlinien nicht bis an den Rand der Box
# reichen.
# Dies ist absichtlich. Die Z-Werte werden im Zentrum jedes
# Bildpixels (jedes Farbbereichs auf dem folgenden Subplot) definiert,
# so dass die konturierte Domäne nicht über diese Pixelzentren hinaus
# reicht.
im = axs[3].imshow(Z, interpolation='nearest', extent=extent,
                   cmap=cmap, norm=norm)
axs[3].contour(Z, levels, colors='k', origin='image', extent=extent)
ylim = axs[3].get_ylim()
axs[3].set_ylim(ylim[::-1])
axs[3].set_title("Ursprung aus rc, umgekehrte y-Achse")
fig.colorbar(im, ax=axs[3])

fig.tight_layout()
plt.show()
```
