# Tracer des régressions polynômes avec les erreurs-types des scores

Les barres d'erreur représentent un écart-type de la distribution gaussienne prédite des points de requête. Remarquez que la régression ARD capture la vérité terrain le mieux en utilisant les paramètres par défaut dans les deux modèles, mais réduire davantage le paramètre hyper `lambda_init` de la Ridge bayésienne peut réduire son biais. Enfin, en raison des limitations intrinsèques d'une régression polynomiale, les deux modèles échouent lors de l'extrapolation.

```python
ax = sns.scatterplot(
    data=full_data, x="input_feature", y="target", color="black", alpha=0.75
)
ax.plot(X_plot, y_plot, color="black", label="Ground Truth")
ax.plot(X_plot, y_brr, color="red", label="BayesianRidge with polynomial features")
ax.plot(X_plot, y_ard, color="navy", label="ARD with polynomial features")
ax.fill_between(
    X_plot.ravel(),
    y_ard - y_ard_std,
    y_ard + y_ard_std,
    color="navy",
    alpha=0.3,
)
ax.fill_between(
    X_plot.ravel(),
    y_brr - y_brr_std,
    y_brr + y_brr_std,
    color="red",
    alpha=0.3,
)
ax.legend()
_ = ax.set_title("Polynomial fit of a non-linear feature")
```
