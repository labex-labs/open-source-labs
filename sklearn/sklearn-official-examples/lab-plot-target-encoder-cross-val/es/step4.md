# Entrenar un regresor Ridge en datos sin codificar

En esta sección, entrenaremos un regresor Ridge en el conjunto de datos con y sin codificación y exploraremos la influencia del codificador de destino con y sin validación cruzada por intervalos. Primero, entrenaremos un modelo Ridge en las características sin procesar. Ejecute el siguiente código para entrenar el modelo Ridge:

```python
ridge = Ridge(alpha=1e-6, solver="lsqr", fit_intercept=False)

raw_model = ridge.fit(X_train, y_train)
print("Raw Model score on training set: ", raw_model.score(X_train, y_train))
print("Raw Model score on test set: ", raw_model.score(X_test, y_test))
```
