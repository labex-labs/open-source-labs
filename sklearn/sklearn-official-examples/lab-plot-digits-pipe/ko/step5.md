# 최적 매개변수 및 점수 출력

GridSearchCV 에서 얻은 최적 매개변수와 점수를 출력합니다.

```python
print("Best parameter (CV score=%0.3f):" % search.best_score_)
print(search.best_params_)
```
