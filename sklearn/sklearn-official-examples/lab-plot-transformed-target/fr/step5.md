# Tracez les valeurs réelles versus les valeurs prédites pour les deux modèles

Nous traçons les valeurs réelles versus les valeurs prédites pour les deux modèles et ajoutons le score dans la légende de chaque axe.

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

ax0.set_title("Régression Ridge \n sans transformation de la cible")
ax1.set_title("Régression Ridge \n avec transformation de la cible")
f.suptitle("Données synthétiques", y=1.05)
plt.tight_layout()
```
