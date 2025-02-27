# Zeichnen von tatsächlichen vs vorhergesagten Werten und Residuen vs vorhergesagten Werten für beide Modelle

Wir zeichnen tatsächliche vs vorhergesagte Werte und Residuen vs vorhergesagte Werte für beide Modelle und fügen die Bewertung in die Legende jeder Achse ein.

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

ax0[0].set_title("Ridge-Regression \n ohne Zieltransformation")
ax0[1].set_title("Ridge-Regression \n mit Zieltransformation")

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
ax1[0].set_title("Ridge-Regression \n ohne Zieltransformation")
ax1[1].set_title("Ridge-Regression \n mit Zieltransformation")

f.suptitle("Ames Wohnungsdaten: Verkaufspreis", y=1.05)
plt.tight_layout()
plt.show()
```
