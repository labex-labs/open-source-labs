# Klebrige Kanten

Einige Diagrammfunktionen in Matplotlib machen die Achsengrenzen "klebrig" oder immun gegen die `margins()`-Methode. Beispielsweise erwarten `imshow()` und `pcolor()`, dass der Benutzer die Grenzen eng um die in der Grafik gezeigten Pixel herum haben möchte. Wenn dieses Verhalten nicht gewünscht ist, müssen Sie `use_sticky_edges` auf `False` setzen. In diesem Schritt werden wir lernen, wie man mit klebrigen Kanten in Matplotlib umgehen kann.

```python
# Erstellen eines Gitters
y, x = np.mgrid[:5, 1:6]

# Definieren von Polygonkoordinaten
poly_coords = [
    (0.25, 2.75), (3.25, 2.75),
    (2.25, 0.75), (0.25, 0.75)
]

# Erstellen von Teilplots
fig, (ax1, ax2) = plt.subplots(ncols=2)

# Verwenden von klebrigen Kanten für ax1 und Deaktivieren von klebrigen Kanten für ax2
ax2.use_sticky_edges = False

# Plotten auf beiden Teilplots
for ax, status in zip((ax1, ax2), ('Ist', 'Ist Nicht')):
    cells = ax.pcolor(x, y, x+y, cmap='inferno', shading='auto') # klebrig
    ax.add_patch(
        Polygon(poly_coords, color='forestgreen', alpha=0.5)
    ) # nicht klebrig
    ax.margins(x=0.1, y=0.05)
    ax.set_aspect('equal')
    ax.set_title(f'{status} Klebrig')

plt.show()
```
