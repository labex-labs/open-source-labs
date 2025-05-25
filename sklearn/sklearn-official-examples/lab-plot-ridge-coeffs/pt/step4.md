# Treinar o modelo com diferentes níveis de regularização

Treinaremos o modelo com diferentes níveis de regularização usando um loop. Definiremos o nível de regularização alterando o valor de alpha na função `set_params`. Guardaremos os coeficientes e os erros para cada valor de alpha.

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
