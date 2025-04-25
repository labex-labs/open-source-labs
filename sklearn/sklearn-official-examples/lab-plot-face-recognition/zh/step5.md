# 训练支持向量机（SVM）分类模型

```python
param_grid = {
    "C": loguniform(1e3, 1e5),
    "gamma": loguniform(1e-4, 1e-1),
}

clf = RandomizedSearchCV(
    SVC(kernel="rbf", class_weight="balanced"), param_grid, n_iter=10
)
clf = clf.fit(X_train_pca, y_train)
```

我们使用变换后的数据训练一个 SVM 分类模型。我们使用`RandomizedSearchCV()`来为 SVM 模型找到最佳超参数。
