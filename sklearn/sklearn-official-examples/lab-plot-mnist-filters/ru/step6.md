# Оценка модели

Мы оценим классификатор MLPClassifier, вычислив его точность на обучающей и тестовой выборках.

```python
print("Training set score: %f" % mlp.score(X_train, y_train))
print("Test set score: %f" % mlp.score(X_test, y_test))
```
