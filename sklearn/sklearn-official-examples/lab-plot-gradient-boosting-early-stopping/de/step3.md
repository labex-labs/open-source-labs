# Modell erstellen und trainieren ohne Early Stopping

Wir werden nun ein Gradient Boosting-Modell erstellen und trainieren, ohne Early Stopping einzusetzen.

```python
gb = ensemble.GradientBoostingClassifier(n_estimators=n_estimators, random_state=0)
start = time.time()
gb.fit(X_train, y_train)
time_gb.append(time.time() - start)
```
