# Importieren der erforderlichen Bibliotheken und Laden von synthetischen Daten

Wir beginnen mit dem Importieren der erforderlichen Bibliotheken und dem Laden von synthetischen Daten. Wir generieren einen synthetischen zufälligen Regressionsdatensatz und modifizieren die Zielwerte, indem wir alle Zielwerte so transformieren, dass alle Einträge nicht-negativ sind, und indem wir eine Exponentialfunktion anwenden, um nicht-lineare Zielwerte zu erhalten, die mit einem einfachen linearen Modell nicht angepasst werden können. Anschließend verwenden wir eine logarithmische (np.log1p) und eine Exponentialfunktion (np.expm1), um die Zielwerte zu transformieren, bevor wir ein lineares Regressionsmodell trainieren und es zur Vorhersage verwenden.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.compose import TransformedTargetRegressor
from sklearn.linear_model import RidgeCV
from sklearn.metrics import median_absolute_error, r2_score, PredictionErrorDisplay

# Generate synthetic data
X, y = make_regression(n_samples=10_000, noise=100, random_state=0)

# Modify the targets
y = np.expm1((y + abs(y.min())) / 200)
y_trans = np.log1p(y)
```
