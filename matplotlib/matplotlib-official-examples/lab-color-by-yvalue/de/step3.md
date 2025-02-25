# Maskierte Arrays erstellen

In diesem Schritt werden wir drei maskierte Arrays erstellen: eines für Werte, die größer als einen bestimmten Schwellenwert sind, eines für Werte, die kleiner als einen bestimmten Schwellenwert sind, und eines für Werte, die zwischen zwei Schwellenwerten liegen.

```python
upper = 0.77
lower = -0.77

supper = np.ma.masked_where(s < upper, s)
slower = np.ma.masked_where(s > lower, s)
smiddle = np.ma.masked_where((s < lower) | (s > upper), s)
```
