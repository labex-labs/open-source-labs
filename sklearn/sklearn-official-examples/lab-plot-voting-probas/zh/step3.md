# 预测所有分类器的类别概率

我们将使用 `predict_proba()` 函数预测所有分类器的类别概率。

```python
probas = [c.fit(X, y).predict_proba(X) for c in (clf1, clf2, clf3, eclf)]
```
