# Graficar valores reales vs valores predichos para ambos modelos

Graficamos los valores reales vs los valores predichos para ambos modelos y agregamos la puntuación en la leyenda de cada eje.

```python
f, (ax0, ax1) = plt.subplots(1, 2, sharey=True)

PredictionErrorDisplay.from_predictions(
    y_test,
    y_pred_ridge,
    kind="actual_vs_predicted",
    ax=ax0,
    scatter_kwargs={"alpha": 0.5},
)
PredictionErrorDisplay.from_predictions(
    y_test,
    y_pred_ridge_with_trans_target,
    kind="actual_vs_predicted",
    ax=ax1,
    scatter_kwargs={"alpha": 0.5},
)

for ax, y_pred in zip([ax0, ax1], [y_pred_ridge, y_pred_ridge_with_trans_target]):
    for name, score in score.items():
        ax.plot([], [], " ", label=f"{name}={score}")
    ax.legend(loc="upper left")

ax0.set_title("Regresión Ridge \n sin transformación de objetivo")
ax1.set_title("Regresión Ridge \n con transformación de objetivo")
f.suptitle("Datos sintéticos", y=1.05)
plt.tight_layout()
```
