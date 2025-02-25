# Konvertieren eines strukturierten Arrays in ein Rekordarray

Wir können ein strukturiertes Array in ein Rekordarray umwandeln, indem wir die `view`-Methode verwenden und den `np.recarray`-Typ angeben.

```python
# Konvertieren eines strukturierten Arrays in ein Rekordarray
recordarr = x.view(np.recarray)
```
