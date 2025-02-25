# Konvertieren eines Rekordarrays in ein strukturiertes Array

Um ein Rekordarray wieder in ein strukturiertes Array umzuwandeln, können wir die `view`-Methode verwenden und den ursprünglichen Datentyp des strukturierten Arrays angeben.

```python
# Konvertieren eines Rekordarrays in ein strukturiertes Array
x = recordarr.view(dtype=[('name', 'U10'), ('age', int)])
```
