# Calcular los errores de entrenamiento y prueba

Calcularemos los errores de entrenamiento y prueba usando el modelo de regresión Elastic-Net de Scikit-learn. Estableceremos el parámetro de regularización `alpha` en un rango de valores de 10^-5 a 10^1 usando `np.logspace()`. También estableceremos `l1_ratio` en 0.7 y `max_iter` en 10000.

```python
alphas = np.logspace(-5, 1, 60)
enet = linear_model.ElasticNet(l1_ratio=0.7, max_iter=10000)
train_errors = list()
test_errors = list()
for alpha in alphas:
    enet.set_params(alpha=alpha)
    enet.fit(X_train, y_train)
    train_errors.append(enet.score(X_train, y_train))
    test_errors.append(enet.score(X_test, y_test))

i_alpha_optim = np.argmax(test_errors)
alpha_optim = alphas[i_alpha_optim]
print("Optimal regularization parameter : %s" % alpha_optim)
```
