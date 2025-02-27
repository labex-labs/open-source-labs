# Importieren von erforderlichen Bibliotheken und Generieren von Daten

Der erste Schritt besteht darin, die erforderlichen Bibliotheken zu importieren und Daten zu generieren. Wir werden numpy und matplotlib verwenden, um Daten zu generieren und zu visualisieren, und scikit-learn, um das One-Class SVM-Modell zu erstellen.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# Generiere Trainingsdaten
X = 0.3 * np.random.randn(100, 2)
X_train = np.r_[X + 2, X - 2]

# Generiere einige reguläre neuartige Beobachtungen
X = 0.3 * np.random.randn(20, 2)
X_test = np.r_[X + 2, X - 2]

# Generiere einige abnorme neuartige Beobachtungen
X_outliers = np.random.uniform(low=-4, high=4, size=(20, 2))
```
