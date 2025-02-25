# Anpassen der Umwandlung

Das Argument `converters` ermöglicht es uns, Umwandlungsfunktionen zu definieren, um komplexere Umwandlungen zu behandeln. Es akzeptiert ein Wörterbuch mit Spaltenindizes oder Spaltennamen als Schlüssel und Umwandlungsfunktionen als Werte.

```python
convertfunc = lambda x: float(x.strip(b"%"))/100.
np.genfromtxt(StringIO(data), converters={1: convertfunc})
```
