# 执行主成分分析（PCA）

我们将通过初始化 PCA 类的一个实例并将其拟合到数据上来对鸢尾花数据集执行主成分分析（PCA）。

```python
pca = PCA(n_components=n_components)
X_pca = pca.fit_transform(X)
```
