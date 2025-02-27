# GPR-Beispiele

GPR mit Schätzung des Rauschpegels: In diesem Beispiel wird GPR mit einem Summen-Kern veranschaulicht, der einen WhiteKernel zur Schätzung des Rauschpegels der Daten enthält.

```python
from sklearn.gaussian_process.kernels import WhiteKernel

# Erstellen eines GPR-Modells mit einem RBF-Kern und einem WhiteKernel
kernel = RBF() + WhiteKernel()
model = GaussianProcessRegressor(kernel=kernel)

# Anpassen des Modells an die Trainingsdaten
model.fit(X_train, y_train)

# Vorhersage mit dem trainierten Modell
y_pred = model.predict(X_test)
```

Vergleich von GPR und Kernel Ridge Regression: Sowohl die Kernel Ridge Regression (KRR) als auch die GPR lernen eine Zielfunktion mithilfe des "Kernel Tricks". Die GPR lernt ein generatives, probabilistisches Modell und kann Konfidenzintervalle liefern, während die KRR nur Vorhersagen liefert.

```python
from sklearn.kernel_ridge import KernelRidge

# Erstellen eines Kernel Ridge Regression-Modells
krr_model = KernelRidge(kernel='rbf')

# Anpassen des KRR-Modells an die Trainingsdaten
krr_model.fit(X_train, y_train)

# Vorhersage mit dem KRR-Modell
krr_y_pred = krr_model.predict(X_test)

# Vergleich der Ergebnisse mit GPR
gpr_model = GaussianProcessRegressor(kernel=RBF())
gpr_model.fit(X_train, y_train)
gpr_y_pred = gpr_model.predict(X_test)
```

GPR auf Mauna Loa CO2-Daten: In diesem Beispiel wird die komplexe Kernel-Engineering und die Hyperparameter-Optimierung mithilfe des Gradientenanstiegs auf der logarithmischen marginalen Wahrscheinlichkeit demonstriert. Die Daten bestehen aus monatlichen Durchschnittskonzentrationen von atmosphärischem CO2, die am Mauna Loa Observatorium in Hawaii gesammelt wurden. Das Ziel ist, die CO2-Konzentration als Funktion der Zeit zu modellieren.

```python
from sklearn.gaussian_process.kernels import RBF, ExpSineSquared, RationalQuadratic, WhiteKernel

# Erstellen eines GPR-Modells mit einem zusammengesetzten Kern
kernel = 34.4**2 * RBF(length_scale=41.8) + 3.27**2 * RBF(length_scale=180) * ExpSineSquared(length_scale=1.44, periodicity=1) + 0.446**2 * RationalQuadratic(alpha=17.7, length_scale=0.957) + 0.197**2 * RBF(length_scale=0.138) + WhiteKernel(noise_level=0.0336)
model = GaussianProcessRegressor(kernel=kernel)

# Anpassen des Modells an die Daten
model.fit(X_train, y_train)

# Vorhersage mit dem trainierten Modell
y_pred = model.predict(X_test)
```
