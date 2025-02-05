# 使用主成分分析（PCA）对数据集进行投影

主成分分析（PCA）用于将数据集投影到一个新的空间，该空间保留了其大部分原始变化。

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)

X_test_pca = pca.fit(X_train).transform(X_test)
```
