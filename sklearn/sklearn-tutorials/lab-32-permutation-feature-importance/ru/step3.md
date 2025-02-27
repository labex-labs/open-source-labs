# Оценка модели

Теперь мы оценим обученную модель с использованием валидационного набора данных. Метрикой оценки, используемой здесь, является коэффициент детерминации (R - squared score).

```python
# Evaluate the model on the validation set
score = model.score(X_val, y_val)
print("Validation score:", score)
```
