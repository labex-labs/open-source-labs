# t分布随机邻域嵌入（t-distributed Stochastic Neighbor Embedding，t-SNE）

t-SNE是一种流行的流形学习方法，它将数据点的相似度转换为概率。在可视化高维数据方面特别有效。

```python
from sklearn.manifold import TSNE

# 创建t-SNE算法的实例
tsne = TSNE(n_components=2)

# 将算法应用于数据并将数据转换到低维空间
X_transformed = tsne.fit_transform(X)
```
