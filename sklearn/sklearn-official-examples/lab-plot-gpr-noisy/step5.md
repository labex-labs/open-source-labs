# Gaussian Process Regression

In this step, we will create a Gaussian process regressor using an additive kernel adding a RBF and WhiteKernel kernels. The WhiteKernel is a kernel that will be able to estimate the amount of noise present in the data while the RBF will serve at fitting the non-linearity between the data and the target.

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


