# Erstellen des Diagramms

Wir erstellen ein 4x3-Diagrammnetz, um die hügelnischen Darstellungen mit verschiedenen Mischmodi und vertikalen Vergrößerungen anzuzeigen. Wir zeigen in der ersten Zeile zunächst das hügelnische Intensitätsbild und platzieren dann in den verbleibenden Zeilen hügelnische Darstellungen mit verschiedenen Mischmodi. Wir verwenden eine for-Schleife, um durch die verschiedenen vertikalen Vergrößerungswerte und Mischmodi zu iterieren.

```python
fig, axs = plt.subplots(nrows=4, ncols=3, figsize=(8, 9))
plt.setp(axs.flat, xticks=[], yticks=[])

for col, ve in zip(axs.T, [0.1, 1, 10]):
    col[0].imshow(ls.hillshade(z, vert_exag=ve, dx=dx, dy=dy), cmap='gray')
    for ax, mode in zip(col[1:], ['hsv', 'overlay','soft']):
        rgb = ls.shade(z, cmap=cmap, blend_mode=mode,
                       vert_exag=ve, dx=dx, dy=dy)
        ax.imshow(rgb)
```
