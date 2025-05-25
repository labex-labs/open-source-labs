# Treinar um Regressor Ridge em Dados Brutos

Nesta seção, treinaremos um regressor Ridge no conjunto de dados com e sem codificação e exploraremos a influência do codificador de destino com e sem a validação cruzada por intervalos. Primeiro, treinaremos um modelo Ridge nas características brutas. Execute o código a seguir para treinar o modelo Ridge:

```python
ridge = Ridge(alpha=1e-6, solver="lsqr", fit_intercept=False)

raw_model = ridge.fit(X_train, y_train)
print("Raw Model score on training set: ", raw_model.score(X_train, y_train))
print("Raw Model score on test set: ", raw_model.score(X_test, y_test))
```
