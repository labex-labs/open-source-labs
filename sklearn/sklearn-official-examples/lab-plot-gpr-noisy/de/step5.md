# Gaussian-Prozess-Regression

In diesem Schritt werden wir einen Gaussian-Prozess-Regressor erstellen, indem wir einen additiven Kernel verwenden, der einen RBF- und einen WhiteKernel-Kernel hinzufügt. Der WhiteKernel ist ein Kernel, der die Menge an Rauschen im Datensatz abschätzen kann, während der RBF dazu dient, die Nichtlinearität zwischen den Daten und dem Ziel anzupassen.

```python
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel

kernel = 1.0 * RBF(length_scale=1e-1, length_scale_bounds=(1e-2, 1e3)) + WhiteKernel(
    noise_level=1e-2, noise_level_bounds=(1e-10, 1e1)
)
gpr = GaussianProcessRegressor(kernel=kernel, alpha=0.0)
gpr.fit(X_train, y_train)
y_mean, y_std = gpr.predict(X, return_std=True)
```
