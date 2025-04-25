# 训练模型

我们将使用带有 L1 惩罚的逻辑回归和 SAGA 算法来训练模型。我们将把`C`的值设置为 50.0 除以训练样本的数量。

```python
# Turn up tolerance for faster convergence
clf = LogisticRegression(C=50.0 / train_samples, penalty="l1", solver="saga", tol=0.1)
clf.fit(X_train, y_train)
```
