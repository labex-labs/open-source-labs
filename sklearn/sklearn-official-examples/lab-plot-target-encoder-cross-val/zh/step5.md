# 使用交叉验证训练岭回归模型

接下来，我们将创建一个包含 `TargetEncoder` 和岭回归模型的管道。该管道使用 `TargetEncoder.fit_transform`，它会使用交叉验证。运行以下代码以使用交叉验证训练岭回归模型：

```python
model_with_cv = make_pipeline(TargetEncoder(random_state=0), ridge)
model_with_cv.fit(X_train, y_train)
print("Model with CV on training set: ", model_with_cv.score(X_train, y_train))
print("Model with CV on test set: ", model_with_cv.score(X_test, y_test))
```
