# Методы с ядром: ядровая регрессия и гауссовский процесс

#### Ядровая регрессия

Мы используем `KernelRidge` с ядром `ExpSineSquared`, которое позволяет восстановить периодичность.

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
    "Kernel ridge regression with an exponential sine squared\n "
    "kernel using default hyperparameters"
)
```

#### Гауссовская процессная регрессия

Мы используем `GaussianProcessRegressor` для подгонки того же набора данных. При обучении гауссовского процесса гиперпараметры ядра оптимизируются в процессе подгонки.

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
_ = plt.title("Gaussian process regressor")

```
