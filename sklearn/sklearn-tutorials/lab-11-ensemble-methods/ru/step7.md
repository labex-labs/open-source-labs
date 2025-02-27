# Оценка классификатора случайного леса (Random Forest Classifier)

Оценим классификатор случайного леса, вычислив точность (accuracy score) на тестовых данных.

```python
accuracy = random_forest.score(X_test, y_test)
print(f"Random Forest Classifier Accuracy: {accuracy}")
```
