# Plotten von Polynomregressionen mit Standardfehlern der Scores

Die Fehlerbalken repräsentieren eine Standardabweichung der vorhergesagten gaussianischen Verteilung der Abfragepunkte. Beachten Sie, dass die ARD-Regression die tatsächliche Situation am besten erfasst, wenn die Standardparameter in beiden Modellen verwendet werden, aber die weitere Reduzierung des Hyperparameters `lambda_init` der Bayesian Ridge ihre Bias reduzieren kann. Schließlich scheitern beide Modelle bei der Extrapolation aufgrund der intrinsischen Limitationen einer Polynomregression.

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
