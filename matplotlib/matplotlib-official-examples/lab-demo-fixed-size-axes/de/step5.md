# Achsen zur Figur hinzufügen

Wir werden die Achsen zur Figur hinzufügen, indem wir die `add_axes()`-Funktion verwenden und die Position des `Divider`-Objekts übergeben.

```python
ax = fig.add_axes(divider.get_position(),
                  axes_locator=divider.new_locator(nx=1, ny=1))
```
