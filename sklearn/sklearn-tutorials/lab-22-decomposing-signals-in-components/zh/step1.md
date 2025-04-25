# 主成分分析（PCA）

#### 精确 PCA 和概率解释

主成分分析（PCA）用于将多变量数据集分解为一组连续的正交分量，这些分量能够解释最大量的方差。可以使用 scikit-learn 中的`PCA`类来实现 PCA。`fit`方法用于学习这些分量，而`transform`方法可用于将新数据投影到这些分量上。

```python
from sklearn.decomposition import PCA

# 创建一个 PCA 对象，n_components 为所需的分量数量
pca = PCA(n_components=2)

# 将 PCA 模型拟合到数据上
pca.fit(data)

# 通过将数据投影到学习到的分量上来转换数据
transformed_data = pca.transform(data)
```
