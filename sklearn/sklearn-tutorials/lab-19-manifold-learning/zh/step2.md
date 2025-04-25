# 局部线性嵌入（Locally Linear Embedding，LLE）

局部线性嵌入（Locally Linear Embedding，LLE）是另一种流形学习算法。它寻求数据的低维投影，以保留局部邻域内的距离。

```python
from sklearn.manifold import LocallyLinearEmbedding

# 创建 LLE 算法的实例
lle = LocallyLinearEmbedding(n_components=2)

# 将算法应用于数据并将数据转换到低维空间
X_transformed = lle.fit_transform(X)
```
