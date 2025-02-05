# 使用期望最大化算法拟合高斯混合模型

我们将使用期望最大化算法拟合一个具有10个分量的经典高斯混合模型。

```python
# 使用期望最大化算法拟合一个具有10个分量的高斯混合模型
gmm = mixture.GaussianMixture(
    n_components=10, covariance_type="full", max_iter=100
).fit(X)
```
