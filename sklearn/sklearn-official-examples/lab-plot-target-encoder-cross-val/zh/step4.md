# 在原始数据上训练岭回归模型

在本节中，我们将在编码和未编码的数据集上训练岭回归模型，并探讨目标编码器在有无区间交叉验证情况下的影响。首先，我们将在原始特征上训练岭回归模型。运行以下代码来训练岭回归模型：

```python
ridge = Ridge(alpha=1e-6, solver="lsqr", fit_intercept=False)

raw_model = ridge.fit(X_train, y_train)
print("Raw Model score on training set: ", raw_model.score(X_train, y_train))
print("Raw Model score on test set: ", raw_model.score(X_test, y_test))
```
