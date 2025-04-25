# 执行主成分分析（PCA）

```python
n_components = 150

pca = PCA(n_components=n_components, svd_solver="randomized", whiten=True).fit(X_train)
eigenfaces = pca.components_.reshape((n_components, h, w))

X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
```

我们执行主成分分析（PCA）以从输入数据中提取特征。我们将成分数量设置为 150，并将 PCA 模型拟合到训练数据上。然后，我们得到特征脸，并将输入数据转换为主成分。
