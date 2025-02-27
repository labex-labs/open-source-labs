# Importieren von erforderlichen Bibliotheken und Generieren von Daten

Zunächst müssen wir die erforderlichen Bibliotheken importieren und einen Datensatz generieren, der für die Klassifizierung geeignet ist. In diesem Beispiel werden wir 50 trennbare Punkte mit der Funktion `make_blobs` aus Scikit-learn generieren.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.datasets import make_blobs

# wir erstellen 50 trennbare Punkte
X, Y = make_blobs(n_samples=50, centers=2, random_state=0, cluster_std=0.60)
```
