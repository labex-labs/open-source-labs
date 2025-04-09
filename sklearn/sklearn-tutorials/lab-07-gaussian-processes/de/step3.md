# Gaussian Process Classification (GPC)

Die GaussianProcessClassifier-Klasse implementiert die GPC für die probabilistische Klassifizierung. Sie legt einen GP-Prior auf eine latente Funktion fest, die dann durch eine Link-Funktion abgesquasht wird, um die Klassenwahrscheinlichkeiten zu erhalten. Die GPC unterstützt die Mehrklassen-Klassifizierung, indem sie entweder eine One-versus-rest- oder eine One-versus-one-Basierte-Trainings- und Vorhersage durchführt.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

X = np.linspace(0, 10, 100).reshape(-1, 1)
y = np.sin(X).ravel() + np.random.normal(0, 0.1, X.shape[0])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.gaussian_process import GaussianProcessClassifier
# Erstellen eines GPC-Modells mit einem RBF-Kern
kernel = RBF()
model = GaussianProcessClassifier(kernel=kernel)

# Anpassen des Modells an die Trainingsdaten
model.fit(X_train, y_train)

# Vorhersage mit dem trainierten Modell
y_pred = model.predict(X_test)
```
