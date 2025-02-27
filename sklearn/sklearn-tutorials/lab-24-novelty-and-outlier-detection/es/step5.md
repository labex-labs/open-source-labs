# Predecir valores atípicos

Una vez que el modelo está ajustado, podemos utilizar el método `predict` para predecir si nuevas observaciones son valores atípicos o no. El método `predict` devuelve 1 para los valores no atípicos y -1 para los valores atípicos.

```python
X_test = [5.5, 8.5]
predictions = estimator.predict(X_test)
print(predictions)
```
