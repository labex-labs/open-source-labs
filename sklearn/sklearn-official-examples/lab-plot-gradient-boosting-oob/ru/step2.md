# Подгонка классификатора с OOB-оценками

Далее мы создадим классификатор градиентного бустинга с OOB-оценками с использованием класса `GradientBoostingClassifier` из модуля `sklearn.ensemble`. Мы установим количество оценщиков равным 100 и скорость обучения равной 0,1.

```python
from sklearn.ensemble import GradientBoostingClassifier

params = {
    "n_estimators": 100,
    "learning_rate": 0.1,
    "subsample": 1.0,
    "max_depth": 3,
    "min_samples_leaf": 1,
    "random_state": 1,
    "oob_score": True
}

clf = GradientBoostingClassifier(**params)
clf.fit(X, y)
```
