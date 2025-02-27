# Построение и обучение модели без раннего прекращения

Теперь мы построим и обучим модель градиентного бустинга без раннего прекращения.

```python
gb = ensemble.GradientBoostingClassifier(n_estimators=n_estimators, random_state=0)
start = time.time()
gb.fit(X_train, y_train)
time_gb.append(time.time() - start)
```
