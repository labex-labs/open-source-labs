# 打印最佳参数和分数

我们将打印从 GridSearchCV 获得的最佳参数和分数。

```python
print("Best parameter (CV score=%0.3f):" % search.best_score_)
print(search.best_params_)
```
