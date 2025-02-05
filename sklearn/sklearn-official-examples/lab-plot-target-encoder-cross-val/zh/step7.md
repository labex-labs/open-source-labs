# 不使用交叉验证训练岭回归模型

虽然 `TargetEncoder.fit_transform` 使用区间交叉验证，但 `TargetEncoder.transform` 本身并不执行任何交叉验证。它使用完整训练集的聚合来转换分类特征。因此，我们可以使用 `TargetEncoder.fit` 后跟 `TargetEncoder.transform` 来禁用交叉验证。然后将这种编码传递给岭回归模型。运行以下代码以不使用交叉验证训练岭回归模型：

```python
target_encoder = TargetEncoder(random_state=0)
target_encoder.fit(X_train, y_train)
X_train_no_cv_encoding = target_encoder.transform(X_train)
X_test_no_cv_encoding = target_encoder.transform(X_test)

model_no_cv = ridge.fit(X_train_no_cv_encoding, y_train)
print(
    "Model without CV on training set: ",
    model_no_cv.score(X_train_no_cv_encoding, y_train),
)
print(
    "Model without CV on test set: ", model_no_cv.score(X_test_no_cv_encoding, y_test)
)
```
