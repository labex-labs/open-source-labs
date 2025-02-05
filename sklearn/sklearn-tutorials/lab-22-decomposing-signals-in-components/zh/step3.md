# 非负矩阵分解（NMF）

#### 基于弗罗贝尼乌斯范数的NMF

非负矩阵分解（NMF）是一种分解方法，它假设数据和分量都是非负的。通过优化数据与两个矩阵乘积之间的距离，它将数据分解为两个非负元素的矩阵。可以使用scikit-learn中的`NMF`类来实现NMF。

```python
from sklearn.decomposition import NMF

# 创建一个NMF对象，n_components为所需的分量数量
nmf = NMF(n_components=2)

# 将NMF模型拟合到数据上
nmf.fit(data)

# 将数据分解为两个非负矩阵
矩阵_W = nmf.transform(data)
矩阵_H = nmf.components_
```
