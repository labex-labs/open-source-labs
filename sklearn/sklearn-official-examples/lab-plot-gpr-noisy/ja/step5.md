# ガウス過程回帰

このステップでは、RBF と WhiteKernel カーネルを加えた加算型カーネルを使用してガウス過程回帰器を作成します。WhiteKernel は、データに含まれるノイズの量を推定できるカーネルであり、RBF は、データとターゲットの間の非線形性を適合させるために役立ちます。

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
