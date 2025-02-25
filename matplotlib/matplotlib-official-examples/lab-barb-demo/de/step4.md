# Windbubenplot anpassen

Wir können den Windbubenplot anpassen, indem wir die Parameter der `barbs`-Funktion ändern. Beispielsweise können wir die Länge und den Drehpunkt der Vektoren ändern, die Kreise für eine leere Bube ausfüllen und die Farben der Flaggen und Stäbe ändern.

```python
plt.barbs(X, Y, U, V, length=8, pivot='middle', fill_empty=True, rounding=False,
          sizes=dict(emptybarb=0.25, spacing=0.2, height=0.3), flagcolor='r',
          barbcolor=['b', 'g'], flip_barb=True, barb_increments=dict(half=10, full=20, flag=100))
plt.show()
```
