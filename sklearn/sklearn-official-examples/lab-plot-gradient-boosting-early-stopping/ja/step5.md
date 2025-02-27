# 早期終了有無でのスコア比較

ここでは、2つのモデルのスコアを比較します。

```python
score_gb.append(gb.score(X_test, y_test))
score_gbes.append(gbes.score(X_test, y_test))
```
