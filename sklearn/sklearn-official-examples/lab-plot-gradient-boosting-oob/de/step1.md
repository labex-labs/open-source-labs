# Daten generieren

Der erste Schritt besteht darin, einige Beispiel-Daten zu generieren, die wir verwenden können, um unser Modell zu trainieren und zu testen. Wir werden die Funktion `make_classification` aus dem Modul `sklearn.datasets` verwenden, um ein zufälliges binäres Klassifizierungsproblem mit 3 informativen Merkmalen zu generieren.

```python
import numpy as np
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=1000, n_features=3, n_informative=3,
                           n_redundant=0, n_classes=2, random_state=1)
```
