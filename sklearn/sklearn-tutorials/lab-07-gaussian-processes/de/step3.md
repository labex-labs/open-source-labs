# Gaussian Process Classification (GPC)

Die GaussianProcessClassifier-Klasse implementiert die GPC für die probabilistische Klassifizierung. Sie legt einen GP-Prior auf eine latente Funktion fest, die dann durch eine Link-Funktion abgesquasht wird, um die Klassenwahrscheinlichkeiten zu erhalten. Die GPC unterstützt die Mehrklassen-Klassifizierung, indem sie entweder eine One-versus-rest- oder eine One-versus-one-Basierte-Trainings- und Vorhersage durchführt.

```python
from sklearn.gaussian_process import GaussianProcessClassifier

# Erstellen eines GPC-Modells mit einem RBF-Kern
kernel = RBF()
model = GaussianProcessClassifier(kernel=kernel)

# Anpassen des Modells an die Trainingsdaten
model.fit(X_train, y_train)

# Vorhersage mit dem trainierten Modell
y_pred = model.predict(X_test)
```
