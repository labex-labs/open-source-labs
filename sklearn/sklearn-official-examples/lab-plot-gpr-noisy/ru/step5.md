# Гауссовский процесс регрессии

В этом шаге мы создадим регрессор Гауссовского процесса с использованием аддитивного ядра, добавляя ядра RBF и WhiteKernel. WhiteKernel - это ядро, которое сможет оценить количество шума, присутствующего в данных, в то время как RBF будет использоваться для подгонки нелинейности между данными и целевым значением.

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
