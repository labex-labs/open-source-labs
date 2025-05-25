# 가우시안 프로세스 회귀

이 단계에서는 덧셈 커널을 사용하여 가우시안 프로세스 회귀 모델을 생성합니다. 덧셈 커널은 RBF 커널과 WhiteKernel 커널을 포함합니다. WhiteKernel 커널은 데이터에 존재하는 노이즈의 양을 추정하는 데 사용되며, RBF 커널은 데이터와 목표 변수 사이의 비선형성을 적합하는 데 사용됩니다.

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
