# Evaluar el modelo

Evaluaremos el MLPClassifier calculando su precisión en los conjuntos de entrenamiento y prueba.

```python
print("Training set score: %f" % mlp.score(X_train, y_train))
print("Test set score: %f" % mlp.score(X_test, y_test))
```
