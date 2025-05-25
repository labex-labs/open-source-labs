# Regressão de Quantil

Usaremos a classe `QuantileRegressor` para estimar a mediana, bem como um quantil baixo e um quantil alto fixados em 5% e 95%, respectivamente. Usaremos os quantis em 5% e 95% para encontrar os valores discrepantes na amostra de treinamento além do intervalo central de 90%.

```python
from sklearn.linear_model import QuantileRegressor

# Esta linha visa evitar incompatibilidades se houver versões mais antigas do SciPy.
# Você deve usar `solver="highs"` com versões recentes do SciPy.
solver = "highs" if sp_version >= parse_version("1.6.0") else "interior-point"

quantiles = [0.05, 0.5, 0.95]
predictions = {}
out_bounds_predictions = np.zeros_like(y_true_mean, dtype=np.bool_)
for quantile in quantiles:
    qr = QuantileRegressor(quantile=quantile, alpha=0, solver=solver)
    y_pred = qr.fit(X, y_normal).predict(X)
    predictions[quantile] = y_pred

    if quantile == min(quantiles):
        out_bounds_predictions = np.logical_or(
            out_bounds_predictions, y_pred >= y_normal
        )
    elif quantile == max(quantiles):
        out_bounds_predictions = np.logical_or(
            out_bounds_predictions, y_pred <= y_normal
        )

plt.plot(X, y_true_mean, color="black", linestyle="dashed", label="Média Verdadeira")

for quantile, y_pred in predictions.items():
    plt.plot(X, y_pred, label=f"Quantil: {quantile}")

plt.scatter(
    x[out_bounds_predictions],
    y_normal[out_bounds_predictions],
    color="black",
    marker="+",
    alpha=0.5,
    label="Fora do intervalo",
)
plt.scatter(
    x[~out_bounds_predictions],
    y_normal[~out_bounds_predictions],
    color="black",
    alpha=0.5,
    label="Dentro do intervalo",
)

plt.legend()
plt.xlabel("x")
plt.ylabel("y")
_ = plt.title("Quantil de alvo distribuído normalmente heterocedástico")

quantiles = [0.05, 0.5, 0.95]
predictions = {}
out_bounds_predictions = np.zeros_like(y_true_mean, dtype=np.bool_)
for quantile in quantiles:
    qr = QuantileRegressor(quantile=quantile, alpha=0, solver=solver)
    y_pred = qr.fit(X, y_pareto).predict(X)
    predictions[quantile] = y_pred

    if quantile == min(quantiles):
        out_bounds_predictions = np.logical_or(
            out_bounds_predictions, y_pred >= y_pareto
        )
    elif quantile == max(quantiles):
        out_bounds_predictions = np.logical_or(
            out_bounds_predictions, y_pred <= y_pareto
        )

plt.plot(X, y_true_mean, color="black", linestyle="dashed", label="Média Verdadeira")

for quantile, y_pred in predictions.items():
    plt.plot(X, y_pred, label=f"Quantil: {quantile}")

plt.scatter(
    x[out_bounds_predictions],
    y_pareto[out_bounds_predictions],
    color="black",
    marker="+",
    alpha=0.5,
    label="Fora do intervalo",
)
plt.scatter(
    x[~out_bounds_predictions],
    y_pareto[~out_bounds_predictions],
    color="black",
    alpha=0.5,
    label="Dentro do intervalo",
)

plt.legend()
plt.xlabel("x")
plt.ylabel("y")
_ = plt.title("Quantil de alvo distribuído assimétricamente de Pareto")
```
