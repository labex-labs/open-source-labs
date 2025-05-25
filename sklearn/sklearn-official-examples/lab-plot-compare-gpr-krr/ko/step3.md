# 커널 기법: 커널 릿지와 가우시안 프로세스

#### 커널 릿지

주기성을 복구할 수 있는 `ExpSineSquared` 커널을 사용한 `KernelRidge`를 사용합니다.

```python
from sklearn.kernel_ridge import KernelRidge
from sklearn.gaussian_process.kernels import ExpSineSquared

kernel_ridge = KernelRidge(kernel=ExpSineSquared())

kernel_ridge.fit(training_data, training_noisy_target)

plt.plot(data, target, label="True signal", linewidth=2, linestyle="dashed")
plt.scatter(
    training_data,
    training_noisy_target,
    color="black",
    label="Noisy measurements",
)
plt.plot(
    data,
    kernel_ridge.predict(data),
    label="Kernel ridge",
    linewidth=2,
    linestyle="dashdot",
)
plt.legend(loc="lower right")
plt.xlabel("data")
plt.ylabel("target")
_ = plt.title(
    "기본 하이퍼파라미터를 사용한 지수 사인 제곱 커널을 사용한\n 커널 릿지 회귀"
)
```

#### 가우시안 프로세스 회귀

같은 데이터셋에 `GaussianProcessRegressor`를 사용합니다. 가우시안 프로세스를 학습할 때, 커널의 하이퍼파라미터는 학습 과정에서 최적화됩니다.

```python
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import WhiteKernel

kernel = 1.0 * ExpSineSquared(1.0, 5.0, periodicity_bounds=(1e-2, 1e1)) + WhiteKernel(
    1e-1
)
gaussian_process = GaussianProcessRegressor(kernel=kernel)

gaussian_process.fit(training_data, training_noisy_target)

mean_predictions_gpr, std_predictions_gpr = gaussian_process.predict(
    data, return_std=True,
)

plt.plot(data, target, label="True signal", linewidth=2, linestyle="dashed")
plt.scatter(
    training_data,
    training_noisy_target,
    color="black",
    label="Noisy measurements",
)
plt.plot(
    data,
    mean_predictions_gpr,
    label="Gaussian process regressor",
    linewidth=2,
    linestyle="dotted",
)
plt.fill_between(
    data.ravel(),
    mean_predictions_gpr - std_predictions_gpr,
    mean_predictions_gpr + std_predictions_gpr,
    color="tab:green",
    alpha=0.2,
)
plt.legend(loc="lower right")
plt.xlabel("data")
plt.ylabel("target")
_ = plt.title("가우시안 프로세스 회귀")
```
