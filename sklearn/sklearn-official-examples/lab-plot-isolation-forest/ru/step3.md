# Обучение модели

Мы обучим модель Isolation Forest на тренировочных данных.

```python
from sklearn.ensemble import IsolationForest

clf = IsolationForest(max_samples=100, random_state=0)
clf.fit(X_train)
```
