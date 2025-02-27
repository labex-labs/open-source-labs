# Hinzufügen von Zufallsmerkmalen

Wir werden einigen Zufallsmerkmalen zu den ursprünglichen Daten hinzufügen, um die von dem Lasso-Modell durchgeführte Merkmalsauswahl besser zu veranschaulichen. Zufallsmerkmale werden mithilfe der Funktion `RandomState` aus `numpy` generiert.

```python
import numpy as np
import pandas as pd

rng = np.random.RandomState(42)
n_random_features = 14
X_random = pd.DataFrame(
    rng.randn(X.shape[0], n_random_features),
    columns=[f"random_{i:02d}" for i in range(n_random_features)],
)
X = pd.concat([X, X_random], axis=1)
X[X.columns[::3]].head()
```
