# Оценка бэггинг-классификатора (Bagging Classifier)

Оценим бэггинг-классификатор, вычислив точность (accuracy score) на тестовых данных с использованием метода `score`.

```python
accuracy = bagging.score(X_test, y_test)
print(f"Bagging Classifier Accuracy: {accuracy}")
```
