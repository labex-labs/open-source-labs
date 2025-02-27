# Swiss-Hole-Datensatz generieren

Wir generieren den Swiss-Hole-Datensatz, indem wir einem Swiss Roll-Datensatz ein Loch hinzufügen, indem wir das Parameter `hole=True` in der Funktion `make_swiss_roll()` verwenden.

```python
sh_points, sh_color = datasets.make_swiss_roll(n_samples=1500, hole=True, random_state=0)
```
