# Создаем модель SVM

Мы создадим линейную модель SVM с использованием обучения SGD.

```python
# create SVM model with SGD training
clf = SGDClassifier(loss="hinge", penalty="elasticnet", fit_intercept=True)
```
