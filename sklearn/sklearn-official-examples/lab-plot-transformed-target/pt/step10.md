# Plotar valores reais vs. valores preditos e resíduos vs. valores preditos para ambos os modelos

Plotamos os valores reais vs. valores preditos e os resíduos vs. valores preditos para ambos os modelos e adicionamos a pontuação na legenda de cada eixo.

```python
f, (ax0, ax1) = plt.subplots(2, 2, sharey="row", figsize=(6.5, 8))

PredictionErrorDisplay.from_predictions(
    y_test,
    y_pred_ridge,
    kind="actual_vs_predicted",
    ax=ax0[0],
    scatter_kwargs={"alpha": 0.5},
)
PredictionErrorDisplay.from_predictions(
    y_test,
    y_pred_ridge_with_trans_target,
    kind="actual_vs_predicted",
    ax=ax0[1],
    scatter_kwargs={"alpha": 0.5},
)

for ax, y_pred in zip([ax0[0], ax0[1]], [y_pred_ridge, y_pred_ridge_with_trans_target]):
    for name, score in score.items():
        ax.plot([], [], " ", label=f"{name}={score}")
    ax.legend(loc="upper left")

ax0[0].set_title("Regressão Ridge \n sem transformação de alvo")
ax0[1].set_title("Regressão Ridge \n com transformação de alvo")

PredictionErrorDisplay.from_predictions(
    y_test,
    y_pred_ridge,
    kind="residual_vs_predicted",
    ax=ax1[0],
    scatter_kwargs={"alpha": 0.5},
)
PredictionErrorDisplay.from_predictions(
    y_test,
    y_pred_ridge_with_trans_target,
    kind="residual_vs_predicted",
    ax=ax1[1],
    scatter_kwargs={"alpha": 0.5},
)
ax1[0].set_title("Regressão Ridge \n sem transformação de alvo")
ax1[1].set_title("Regressão Ridge \n com transformação de alvo")

f.suptitle("Dados de habitação de Ames: preço de venda", y=1.05)
plt.tight_layout()
plt.show()
```
