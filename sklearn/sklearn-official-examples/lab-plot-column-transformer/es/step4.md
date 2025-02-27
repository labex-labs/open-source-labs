# Entrenamiento y prueba

Ajustaremos nuestra pipeline a los datos de entrenamiento y la usaremos para predecir los temas de `X_test`. Luego se imprimen las métricas de rendimiento de nuestra pipeline.

```python
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print("Informe de clasificación:\n\n{}".format(classification_report(y_test, y_pred)))
```
