# Maskieren der Daten

In diesem Schritt werden wir einige der `z`-Werte mit einer booleschen Maske maskieren. Wir erstellen ein `mask`-Array mit der Funktion `np.zeros_like()` und setzen dann einige der Werte auf `True`, um sie zu maskieren.

```python
# Mask various z values.
mask = np.zeros_like(z, dtype=bool)
mask[2, 3:5] = True
mask[3:5, 4] = True
mask[7, 2] = True
mask[5, 0] = True
mask[0, 6] = True
z = np.ma.array(z, mask=mask)
```
