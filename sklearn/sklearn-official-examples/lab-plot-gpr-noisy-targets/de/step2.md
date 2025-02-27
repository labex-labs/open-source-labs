# Rauschfreies Ziel

In diesem Schritt werden wir den wahren Generierungsprozess verwenden, ohne irgendeinen Rausch hinzuzufügen. Für das Training der Gaussian Process Regression werden wir nur einige wenige Stichproben auswählen.

```python
rng = np.random.RandomState(1)
training_indices = rng.choice(np.arange(y.size), size=6, replace=False)
X_train, y_train = X[training_indices], y[training_indices]

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF

kernel = 1 * RBF(length_scale=1.0, length_scale_bounds=(1e-2, 1e2))
gaussian_process = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=9)
gaussian_process.fit(X_train, y_train)
gaussian_process.kernel_
```
