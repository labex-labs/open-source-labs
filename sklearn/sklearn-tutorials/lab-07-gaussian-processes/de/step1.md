# Gaussian Process Regression (GPR)

Die GaussianProcessRegressor-Klasse implementiert Gaussian Prozesse für Regressionsaufgaben. Es ist erforderlich, einen Prior für den GP anzugeben, wie z. B. die Mittel- und Kovarianzfunktionen. Die Hyperparameter des Kerns werden während des Anpassungsprozesses optimiert. Schauen wir uns ein Beispiel für die Verwendung von GPR für die Regression an.

```python
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF

# Erstellen eines GPR-Modells mit einem RBF-Kern
kernel = RBF()
model = GaussianProcessRegressor(kernel=kernel)

# Anpassen des Modells an die Trainingsdaten
model.fit(X_train, y_train)

# Vorhersage mit dem trainierten Modell
y_pred = model.predict(X_test)
```
