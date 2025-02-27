# Laden und Vorverarbeiten der Daten

Wir beginnen mit dem Laden des handschriftlichen Ziffern-Datensatzes aus scikit-learn und teilen ihn in Trainings- und Testsets auf. Wir skalieren auch die Daten, um eine mittlere Null und eine Varianz von 1 zu erhalten.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Lade den Ziffern-Datensatz
X, y = datasets.load_digits(return_X_y=True)

# Teile die Daten in Trainings- und Testsets auf
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Skaliere die Daten, um eine mittlere Null und eine Varianz von 1 zu erhalten
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```
