# Daten laden

Als nächstes laden wir die Daten, die wir plotten möchten. Wir verwenden ein numpy-Record-Array aus Yahoo-CSV-Daten mit den Feldern date, open, high, low, close, volume, adj_close aus dem Verzeichnis mpl-data/sample_data. Das Record-Array speichert das Datum als np.datetime64 mit einem Tagesformat ('D') in der date-Spalte.

```python
data = cbook.get_sample_data('goog.npz')['price_data']
```
