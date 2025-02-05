# 拟合高斯混合模型

现在，我们可以使用`sklearn.mixture`模块中的`GaussianMixture`类，将高斯混合模型拟合到我们的数据上。指定所需的组件数量以及你想要使用的任何其他参数。

```python
# 拟合高斯混合模型
gmm = GaussianMixture(n_components=3)
gmm.fit(X_train)
```
