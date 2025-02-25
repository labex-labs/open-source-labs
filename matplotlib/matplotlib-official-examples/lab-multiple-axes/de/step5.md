# Verbindunglinie zeichnen

Der fünfte Schritt besteht darin, eine gestrichelte Linie zu zeichnen, die die beiden Teilplots verbindet. Wir erstellen ein `ConnectionPatch`-Objekt, das den Ursprung des linken Teilplots mit der rechten Kante des rechten Teilplots verbindet. Wir speichern auch das `con`-Patch-Objekt, das wir später in der Animation aktualisieren werden.

```python
con = ConnectionPatch(
    (1, 0),
    (0, 0),
    "data",
    "data",
    axesA=axl,
    axesB=axr,
    color="C0",
    ls="dotted",
)
fig.add_artist(con)
```
