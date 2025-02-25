# Daten erstellen

In diesem Schritt werden wir einige Daten erstellen, die geplottet werden sollen. Wir werden die Funktion `squiggle_xy` verwenden, um einige Sinus- und Kosinuswellen mit unterschiedlichen Frequenzen zu generieren.

```python
def squiggle_xy(a, b, c, d):
    i = np.arange(0.0, 2*np.pi, 0.05)
    return np.sin(i*a)*np.cos(i*b), np.sin(i*c)*np.cos(i*d)
```
