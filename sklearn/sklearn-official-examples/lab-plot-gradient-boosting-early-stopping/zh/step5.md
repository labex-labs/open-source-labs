# 比较有无早期停止时的分数

现在我们将比较这两个模型的分数。

```python
score_gb.append(gb.score(X_test, y_test))
score_gbes.append(gbes.score(X_test, y_test))
```
