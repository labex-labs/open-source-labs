# 使用不同惩罚项和正则化参数训练逻辑回归模型

我们将使用 L1、L2 和弹性网络惩罚以及不同的`C`值来训练逻辑回归模型。为了缩短训练时间，我们将增大容忍度。

```python
for i, (C, axes_row) in enumerate(zip((1, 0.1, 0.01), axes)):
    clf_l1_LR = LogisticRegression(C=C, penalty="l1", tol=0.01, solver="saga")
    clf_l2_LR = LogisticRegression(C=C, penalty="l2", tol=0.01, solver="saga")
    clf_en_LR = LogisticRegression(C=C, penalty="elasticnet", solver="saga", l1_ratio=l1_ratio, tol=0.01)
    clf_l1_LR.fit(X, y)
    clf_l2_LR.fit(X, y)
    clf_en_LR.fit(X, y)
```
