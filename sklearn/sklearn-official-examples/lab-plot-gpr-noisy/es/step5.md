# Regresión con Procesos Gaussianos

En este paso, crearemos un regresor de procesos gaussianos usando un kernel aditivo que agrega los kernels RBF y WhiteKernel. El kernel WhiteKernel es un kernel que será capaz de estimar la cantidad de ruido presente en los datos mientras que el RBF servirá para ajustar la no-linealidad entre los datos y la variable objetivo.

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
