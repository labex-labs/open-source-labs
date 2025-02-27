# Importieren der erforderlichen Bibliotheken und Definition von Konstanten

Zunächst müssen wir die erforderlichen Bibliotheken importieren und die Farben und die Konstante für den Zufallszahlengenerator definieren, um den Mehrfachklassifizierungsdatensatz zu generieren.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_multilabel_classification as make_ml_clf

COLORS = np.array(
    [
        "!",
        "#FF3333",  # rot
        "#0198E1",  # blau
        "#BF5FFF",  # lila
        "#FCD116",  # gelb
        "#FF7216",  # orange
        "#4DBD33",  # grün
        "#87421F",  # braun
    ]
)

# Verwenden Sie denselben Zufallszahlengenerator bei mehreren Aufrufen von
# make_multilabel_classification, um sicherzustellen, dass die Verteilungen gleich sind
RANDOM_SEED = np.random.randint(2**10)
```
