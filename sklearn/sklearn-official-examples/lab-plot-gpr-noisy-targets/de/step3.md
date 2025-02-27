# Vorhersagen und Konfidenzintervalle

Nachdem wir unser Modell angepasst haben, sehen wir, dass die Hyperparameter des Kerns optimiert wurden. Nun werden wir unseren Kern verwenden, um die mittlere Vorhersage des gesamten Datensatzes zu berechnen und das 95%-Konfidenzintervall zu plotten.

```python
mean_prediction, std_prediction = gaussian_process.predict(X, return_std=True)

plt.plot(X, y, label=r"$f(x) = x \sin(x)$", linestyle="dotted")
plt.scatter(X_train, y_train, label="Beobachtungen")
plt.plot(X, mean_prediction, label="Mittlere Vorhersage")
plt.fill_between(
    X.ravel(),
    mean_prediction - 1.96 * std_prediction,
    mean_prediction + 1.96 * std_prediction,
    alpha=0.5,
    label=r"95%-Konfidenzintervall",
)
plt.legend()
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
_ = plt.title("Gaussian process regression on noise-free dataset")
```
