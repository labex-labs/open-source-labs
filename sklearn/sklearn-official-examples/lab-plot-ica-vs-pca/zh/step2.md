# 使用主成分分析（PCA）算法

在这一步中，我们使用主成分分析（PCA）算法在原始特征空间中找到与解释最大方差的方向相对应的正交方向。

```python
pca = PCA()
S_pca_ = pca.fit(X).transform(X)
```
