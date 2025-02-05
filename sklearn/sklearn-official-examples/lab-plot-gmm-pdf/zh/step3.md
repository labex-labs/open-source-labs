# 拟合高斯混合模型

现在，我们将使用scikit-learn中的GaussianMixture类对数据集拟合一个GMM。我们将把组件数量设置为2，协方差类型设置为“full”。

```python
# 拟合一个具有两个组件的高斯混合模型
clf = mixture.GaussianMixture(n_components=2, covariance_type="full")
clf.fit(X_train)
```
