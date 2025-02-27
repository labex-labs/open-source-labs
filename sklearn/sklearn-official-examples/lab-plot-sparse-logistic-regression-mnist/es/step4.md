# Entrenar el modelo

Entrenaremos el modelo usando regresión logística con penalización L1 y el algoritmo SAGA. Estableceremos el valor de `C` en 50.0 dividido por el número de muestras de entrenamiento.

```python
# Turn up tolerance for faster convergence
clf = LogisticRegression(C=50.0 / train_samples, penalty="l1", solver="saga", tol=0.1)
clf.fit(X_train, y_train)
```
