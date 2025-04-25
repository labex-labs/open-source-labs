# 针对艾姆斯房屋数据的原始目标训练并评估线性回归模型

我们针对艾姆斯房屋数据的原始目标训练并评估一个线性回归模型。

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

ridge_cv = RidgeCV().fit(X_train, y_train)
y_pred_ridge = ridge_cv.predict(X_test)

score = {
    "R2": f"{r2_score(y_test, y_pred_ridge):.3f}",
    "MedAE": f"{median_absolute_error(y_test, y_pred_ridge):.3f}",
}

print("\n针对原始目标的线性回归：")
for key, val in score.items():
    print(f"{key}: {val}")
```
