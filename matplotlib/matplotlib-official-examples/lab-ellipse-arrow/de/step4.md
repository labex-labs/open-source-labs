# Die Orientierungsrichtung des Pfeils umkehren

Wenn du die Orientierungsrichtung des Pfeils umkehren möchtest, kannst du den Markertyp von `>` zu `<` wechseln.

```python
# Um die Orientierungsrichtung des Pfeils umzukehren, wechsle den Markertyp von > zu <.
ax.plot(
    vertices[0][0],
    vertices[0][1],
    color="b",
    marker=MarkerStyle("<", "full", t),
    markersize=10
)
```
