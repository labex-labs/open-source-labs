# Füge eine Maßstäbe hinzu

Zeichne eine horizontale Linie mit einer Länge von 0,1 in Datenkoordinaten mit einem festen Label darunter.

```python
asb = AnchoredSizeBar(ax.transData,
                      0.1,
                      r"1$^{\prime}$",
                      loc='lower center',
                      pad=0.1, borderpad=0.5, sep=5,
                      frameon=False)
ax.add_artist(asb)
```
