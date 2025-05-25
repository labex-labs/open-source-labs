# Conclusão Final

Podemos dar uma palavra final sobre a possibilidade dos dois modelos extrapolarem. Observamos que os modelos continuarão a prever o padrão senoidal.

```python
kernel = 1.0 * ExpSineSquared(1.0, 5.0, periodicity_bounds=(1e-2, 1e1)) * RBF(
    length_scale=15, length_scale_bounds="fixed"
) + WhiteKernel(1e-1)
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
_ = plt.title("Comparação entre regressão Kernel Ridge e regressão por processo gaussiano")
```
