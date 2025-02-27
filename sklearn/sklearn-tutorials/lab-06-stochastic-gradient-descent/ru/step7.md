# Оценка производительности

Наконец, мы оценим производительность классификатора, вычислив точность (accuracy) его предсказаний на тестовой выборке.

```python
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
```
