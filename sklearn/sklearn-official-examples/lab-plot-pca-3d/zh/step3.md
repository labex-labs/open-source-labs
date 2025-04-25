# 执行主成分分析（PCA）

接下来，我们将对数据集执行主成分分析（PCA）。我们首先将`x`、`y`和`z`连接起来，形成一个三维数组`Y`。然后，我们创建 PCA 类的一个实例，并将其拟合到我们的数据上。接着，我们可以使用 PCA 对象的`components_`属性来访问主成分。

```python
Y = np.c_[x, y, z]
pca = PCA(n_components=3)
pca.fit(Y)
components = pca.components_
```
