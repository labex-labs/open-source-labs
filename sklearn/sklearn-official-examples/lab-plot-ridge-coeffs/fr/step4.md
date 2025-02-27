# Entraîner le modèle avec différentes forces de régularisation

Nous allons entraîner le modèle avec différentes forces de régularisation en utilisant une boucle. Nous allons définir la force de régularisation en changeant la valeur de alpha dans la fonction `set_params`. Nous allons enregistrer les coefficients et les erreurs pour chaque valeur de alpha.

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
