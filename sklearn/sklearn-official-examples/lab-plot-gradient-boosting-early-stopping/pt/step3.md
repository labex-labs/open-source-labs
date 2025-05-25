# Construir e Treinar o Modelo sem Parada Antecipada

Agora, construiremos e treinaremos um modelo de boosting de gradientes sem parada antecipada.

```python
gb = ensemble.GradientBoostingClassifier(n_estimators=n_estimators, random_state=0)
start = time.time()
gb.fit(X_train, y_train)
time_gb.append(time.time() - start)
```
