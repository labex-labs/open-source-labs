# 高斯过程回归

在这一步中，我们将使用一个加法核来创建一个高斯过程回归器，该加法核添加了一个径向基函数（RBF）核和一个白噪声核（WhiteKernel）。白噪声核是一个能够估计数据中存在的噪声量的核，而径向基函数核将用于拟合数据与目标之间的非线性关系。

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
