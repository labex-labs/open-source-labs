# Importieren von erforderlichen Bibliotheken und Daten

Wir müssen zunächst die erforderlichen Bibliotheken importieren, nämlich `matplotlib`, `numpy` und `matplotlib.cbook`. Wir müssen auch ein numpy-Record-Array aus yahoo-csv-Daten mit den Feldern date, open, high, low, close, volume, adj_close aus dem mpl-data/sample_data-Verzeichnis laden. Das Record-Array speichert das Datum als np.datetime64 mit einem Tagesformat ('D') in der date-Spalte. Wir werden diese Daten verwenden, um die finanzielle Zeitreihe zu plotten.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# Lade Daten aus dem sample_data-Verzeichnis
r = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
r = r[:9]  # Hole die ersten 9 Tage
```
