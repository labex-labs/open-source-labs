# Entrenar el modelo con diferentes valores de regularización

Entrenaremos el modelo con diferentes valores de regularización utilizando un bucle. Estableceremos la fuerza de regularización cambiando el valor de alpha en la función `set_params`. Guardaremos los coeficientes y los errores para cada valor de alpha.

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
