# Regressão por Processo Gaussiano

Nesta etapa, criaremos um regressor de processo gaussiano usando um kernel aditivo que adiciona kernels RBF e WhiteKernel. O WhiteKernel é um kernel que será capaz de estimar a quantidade de ruído presente nos dados, enquanto o RBF servirá para ajustar a não-linearidade entre os dados e o alvo.

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
