# Graficar valores reales vs valores predichos y residuos vs valores predichos para ambos modelos

Graficamos valores reales vs valores predichos y residuos vs valores predichos para ambos modelos y agregamos la puntuación en la leyenda de cada eje.

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

ax0[0].set_title("Regresión Ridge \n sin transformación del objetivo")
ax0[1].set_title("Regresión Ridge \n con transformación del objetivo")

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
ax1[0].set_title("Regresión Ridge \n sin transformación del objetivo")
ax1[1].set_title("Regresión Ridge \n con transformación del objetivo")

f.suptitle("Datos de la vivienda de Ames: precio de venta", y=1.05)
plt.tight_layout()
plt.show()
```
