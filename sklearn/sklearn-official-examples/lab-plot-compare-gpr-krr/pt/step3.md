# Métodos de Kernel: Kernel Ridge e Processo Gaussiano

#### Kernel Ridge

Utilizamos um `KernelRidge` com um kernel `ExpSineSquared`, que permite recuperar a periodicidade.

```python
from sklearn.kernel_ridge import KernelRidge
from sklearn.gaussian_process.kernels import ExpSineSquared

kernel_ridge = KernelRidge(kernel=ExpSineSquared())

kernel_ridge.fit(training_data, training_noisy_target)

plt.plot(data, target, label="Sinal verdadeiro", linewidth=2, linestyle="dashed")
plt.scatter(
    training_data,
    training_noisy_target,
    color="black",
    label="Medições ruidosas",
)
plt.plot(
    data,
    kernel_ridge.predict(data),
    label="Kernel ridge",
    linewidth=2,
    linestyle="dashdot",
)
plt.legend(loc="lower right")
plt.xlabel("Dados")
plt.ylabel("Alvo")
_ = plt.title(
    "Regressão Kernel Ridge com um kernel exponencial seno ao quadrado\n "
    "usando hiperparâmetros padrão"
)
```

#### Regressão por Processo Gaussiano

Utilizamos um `GaussianProcessRegressor` para ajustar o mesmo conjunto de dados. Ao treinar um processo gaussiano, os hiperparâmetros do kernel são otimizados durante o processo de ajuste.

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

plt.plot(data, target, label="Sinal verdadeiro", linewidth=2, linestyle="dashed")
plt.scatter(
    training_data,
    training_noisy_target,
    color="black",
    label="Medições ruidosas",
)
plt.plot(
    data,
    mean_predictions_gpr,
    label="Regressão por Processo Gaussiano",
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
plt.xlabel("Dados")
plt.ylabel("Alvo")
_ = plt.title("Regressão por Processo Gaussiano")
```
