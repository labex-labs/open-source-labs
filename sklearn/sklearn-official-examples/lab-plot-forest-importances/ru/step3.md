# Обучение случайного леса

Мы обучим классификатор случайного леса для вычисления важности признаков.

```python
feature_names = [f"признак {i}" for i in range(X.shape[1])]
forest = RandomForestClassifier(random_state=0)
forest.fit(X_train, y_train)
```
