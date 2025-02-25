# Erstellen der Kugel

Wir werden nun in der Grafik eine Kugel erstellen, indem wir eine Bedingung für die RGB-Werte definieren, die sich innerhalb eines bestimmten Abstands vom Zentrum der Grafik befinden.

```python
rc = midpoints(r)
gc = midpoints(g)
bc = midpoints(b)

sphere = (rc - 0.5)**2 + (gc - 0.5)**2 + (bc - 0.5)**2 < 0.5**2
```
