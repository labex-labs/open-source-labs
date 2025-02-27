# Ledoit-Wolf-Schrumpfung

Die Ledoit-Wolf-Schrumpfungsmethode liefert einen optimalen Schrumpfungskoeffizienten, der den mittleren quadratischen Fehler zwischen der geschätzten und der wahren Kovarianzmatrix minimiert. Das `sklearn.covariance`-Paket enthält eine Funktion `ledoit_wolf`, die verwendet werden kann, um den Ledoit-Wolf-Schätzer für einen gegebenen Datensatz zu berechnen.

```python
from sklearn.covariance import ledoit_wolf

# Compute the Ledoit-Wolf estimator of the covariance matrix
ledoit_wolf_covariance_matrix = ledoit_wolf(data)[0]
```
