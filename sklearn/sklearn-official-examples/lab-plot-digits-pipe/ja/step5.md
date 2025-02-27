# 最適なパラメータとスコアを表示する

GridSearchCV から得られた最適なパラメータとスコアを表示します。

```python
print("Best parameter (CV score=%0.3f):" % search.best_score_)
print(search.best_params_)
```
