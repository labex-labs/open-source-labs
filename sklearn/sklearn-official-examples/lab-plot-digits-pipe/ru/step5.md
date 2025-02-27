# Выводим наилучшие параметры и оценку

Мы выведем наилучшие параметры и оценку, полученные из GridSearchCV.

```python
print("Best parameter (CV score=%0.3f):" % search.best_score_)
print(search.best_params_)
```
