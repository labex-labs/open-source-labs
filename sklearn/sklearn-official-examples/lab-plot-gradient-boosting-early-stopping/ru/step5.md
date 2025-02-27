# Сравнение результатов с и без раннего прекращения

Теперь мы сравним результаты работы двух моделей.

```python
score_gb.append(gb.score(X_test, y_test))
score_gbes.append(gbes.score(X_test, y_test))
```
