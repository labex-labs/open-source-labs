# Construir y entrenar el modelo sin early stopping

Ahora construiremos y entrenaremos un modelo de gradient boosting sin early stopping.

```python
gb = ensemble.GradientBoostingClassifier(n_estimators=n_estimators, random_state=0)
start = time.time()
gb.fit(X_train, y_train)
time_gb.append(time.time() - start)
```
