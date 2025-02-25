# Daten laden

Wir werden ein numpy-Record-Array aus yahoo-csv-Daten laden, die Felder wie Datum, Öffnung, Hoch, Tief, Schluss, Volumen, adjustierter Schluss aus dem mpl-data/sample_data-Verzeichnis haben. Das Record-Array speichert das Datum als np.datetime64 mit einem Tagesformat ('D') in der Datumsspalte.

```python
import matplotlib.cbook as cbook

price_data = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
price_data = price_data[-250:]  # get the most recent 250 trading days
```
