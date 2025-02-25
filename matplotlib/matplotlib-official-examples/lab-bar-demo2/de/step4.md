# Setzen der x- und y-Einheiten für das Balkendiagramm

In diesem Schritt werden wir die x- und y-Einheiten für das Balkendiagramm mit verschiedenen Schlüsselwörtern festlegen. Wir werden die Parameter `xunits` und `yunits` verwenden, um die x- und y-Einheiten auf Zentimeter und Zoll festzulegen.

```python
axs[0, 1].bar(cms, cms, bottom=bottom, width=width, xunits=cm, yunits=inch)
```
