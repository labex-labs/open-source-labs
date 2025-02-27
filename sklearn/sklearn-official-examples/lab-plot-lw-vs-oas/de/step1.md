# Bibliotheken importieren

Zunächst müssen wir die erforderlichen Bibliotheken für dieses Lab importieren. Wir werden `numpy` für numerische Berechnungen, `matplotlib` für Visualisierungen und `scikit-learn` für die Kovarianzschätzung verwenden.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import toeplitz, cholesky
from sklearn.covariance import LedoitWolf, OAS
```
