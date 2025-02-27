# Struktur der Daten definieren

Pixel in einem Bild sind mit ihren Nachbarn verbunden. Um hierarchische Clusteranalyse auf einem Bild durchzuführen, müssen wir die Struktur der Daten definieren. Wir können die `grid_to_graph`-Funktion von scikit-learn verwenden, um eine Verbindungsmatrix zu erstellen, die die Struktur der Daten definiert.

```python
from sklearn.feature_extraction.image import grid_to_graph

connectivity = grid_to_graph(*rescaled_coins.shape)
```
