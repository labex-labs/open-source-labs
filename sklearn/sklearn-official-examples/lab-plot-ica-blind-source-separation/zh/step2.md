# 拟合独立成分分析（ICA）和主成分分析（PCA）模型

我们将使用快速独立成分分析（FastICA）来估计独立源。然后，我们将计算主成分分析（PCA）以作比较。

```python
from sklearn.decomposition import FastICA, PCA

# 计算独立成分分析
ica = FastICA(n_components=3, whiten="arbitrary-variance")
S_ = ica.fit_transform(X)  # 重构信号
A_ = ica.mixing_  # 获取估计的混合矩阵

# 我们可以通过反转解混来“证明”独立成分分析模型是适用的。
assert np.allclose(X, np.dot(S_, A_.T) + ica.mean_)

# 为作比较，计算主成分分析
pca = PCA(n_components=3)
H = pca.fit_transform(X)  # 基于正交成分重构信号
```
