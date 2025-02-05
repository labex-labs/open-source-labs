# 使用随机奇异值分解（Randomized SVD）计算主奇异向量

我们将使用scikit-learn中实现的randomized_svd方法来计算主奇异向量。

```python
from sklearn.decomposition import randomized_svd

print("Computing the principal singular vectors using randomized_svd")
U, s, V = randomized_svd(X, 5, n_iter=3)
```
