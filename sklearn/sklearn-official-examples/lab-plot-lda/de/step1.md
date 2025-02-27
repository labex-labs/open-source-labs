# Zufällige Daten generieren

Zunächst müssen wir zufällige Daten mit einem diskriminierenden Merkmal und rauschenden Merkmalen generieren. Wir werden die `make_blobs`-Funktion von scikit-learn verwenden, um zwei Cluster von Daten mit einem diskriminierenden Merkmal zu generieren. Anschließend werden wir zufälliges Rauschen zu den anderen Merkmalen hinzufügen.

```python
import numpy as np
from sklearn.datasets import make_blobs

def generate_data(n_samples, n_features):
    """Generiert zufällige blob-ähnliche Daten mit rauschenden Merkmalen.

    Dies gibt ein Array mit den Eingabedaten der Form `(n_samples, n_features)`
    und ein Array mit `n_samples` Ziel-Labels zurück.

    Nur ein Merkmal enthält diskriminierende Informationen, die anderen Merkmale
    enthalten nur Rauschen.
    """
    X, y = make_blobs(n_samples=n_samples, n_features=1, centers=[[-2], [2]])

    # füge nicht-diskriminierende Merkmale hinzu
    if n_features > 1:
        X = np.hstack([X, np.random.randn(n_samples, n_features - 1)])
    return X, y
```
