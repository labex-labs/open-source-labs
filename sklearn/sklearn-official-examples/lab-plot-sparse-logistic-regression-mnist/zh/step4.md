# 训练模型

我们将使用带有L1惩罚的逻辑回归和SAGA算法来训练模型。我们将把`C`的值设置为50.0除以训练样本的数量。

```python
# Turn up tolerance for faster convergence
clf = LogisticRegression(C=50.0 / train_samples, penalty="l1", solver="saga", tol=0.1)
clf.fit(X_train, y_train)
```
