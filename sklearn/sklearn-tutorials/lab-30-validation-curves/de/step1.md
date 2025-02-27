# Importieren der erforderlichen Bibliotheken und Laden der Daten

Lassen Sie uns beginnen, indem wir die erforderlichen Bibliotheken importieren und einen Datensatz laden. In diesem Beispiel verwenden wir den Iris-Datensatz.

```python
import numpy as np
from sklearn.model_selection import validation_curve
from sklearn.datasets import load_iris
from sklearn.linear_model import Ridge

np.random.seed(0)
X, y = load_iris(return_X_y=True)
```
