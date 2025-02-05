# 在原始目标上训练并评估线性回归模型

我们在原始目标上训练并评估一个线性回归模型。由于数据的非线性，训练得到的模型在预测时不会很精确。

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

ridge_cv = RidgeCV().fit(X_train, y_train)
y_pred_ridge = ridge_cv.predict(X_test)

score = {
    "R2": f"{r2_score(y_test, y_pred_ridge):.3f}",
    "MedAE": f"{median_absolute_error(y_test, y_pred_ridge):.3f}",
}

print("Linear Regression on original targets:")
for key, val in score.items():
    print(f"{key}: {val}")
```
