# Prédictions et intervalles de confiance

Après avoir ajusté notre modèle, nous voyons que les hyperparamètres du noyau ont été optimisés. Maintenant, nous allons utiliser notre noyau pour calculer la prédiction moyenne de l'ensemble de données complet et tracer l'intervalle de confiance à 95 %.

```python
mean_prediction, std_prediction = gaussian_process.predict(X, return_std=True)

plt.plot(X, y, label=r"$f(x) = x \sin(x)$", linestyle="dotted")
plt.scatter(X_train, y_train, label="Observations")
plt.plot(X, mean_prediction, label="Mean prediction")
plt.fill_between(
    X.ravel(),
    mean_prediction - 1.96 * std_prediction,
    mean_prediction + 1.96 * std_prediction,
    alpha=0.5,
    label=r"95% confidence interval",
)
plt.legend()
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
_ = plt.title("Gaussian process regression on noise-free dataset")
```
