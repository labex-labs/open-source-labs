# Distanzmaße

Distanzmaße sind Funktionen, die die Unähnlichkeit zwischen zwei Objekten messen. Diese Maße erfüllen bestimmte Bedingungen, wie Nichtnegativität, Symmetrie und die Dreiecksungleichung.

Einige bekannte Distanzmaße sind die euklidische Distanz, die Manhattan-Distanz und die Minkowski-Distanz.

Lassen Sie uns die paarweisen Distanzen zwischen zwei Mengen von Proben mit der Funktion `pairwise_distances` berechnen:

```python
import numpy as np
from sklearn.metrics import pairwise_distances

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Calculate pairwise distances between X and Y
distances = pairwise_distances(X, Y, metric='manhattan')
print(distances)
```

Ausgabe:

```
array([[4., 2.],
       [7., 5.],
       [12., 10.]])
```
