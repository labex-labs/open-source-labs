# Trainieren des Modells mit unterschiedlichen Regularisierungswerten

Wir werden das Modell mit unterschiedlichen Regularisierungswerten in einer Schleife trainieren. Wir werden die Regularisierungswert durch Ändern des Wertes von alpha in der `set_params`-Funktion festlegen. Wir werden die Koeffizienten und Fehler für jeden Wert von alpha speichern.

```python
coefs = []
errors = []

alphas = np.logspace(-6, 6, 200)

for a in alphas:
    clf.set_params(alpha=a)
    clf.fit(X, y)
    coefs.append(clf.coef_)
    errors.append(mean_squared_error(clf.coef_, w))
```
