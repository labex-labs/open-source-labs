# Construire et entraîner le modèle sans arrêt précoce

Nous allons maintenant construire et entraîner un modèle de gradient boosting sans arrêt précoce.

```python
gb = ensemble.GradientBoostingClassifier(n_estimators=n_estimators, random_state=0)
start = time.time()
gb.fit(X_train, y_train)
time_gb.append(time.time() - start)
```
