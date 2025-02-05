# 等距映射（Isomap）

等距映射（Isomap）算法是最早的流形学习方法之一。它寻求一种低维嵌入，以保持所有点之间的测地距离。

```python
from sklearn.manifold import Isomap

# 创建等距映射（Isomap）算法的实例
isomap = Isomap(n_components=2)

# 将算法应用于数据并将数据转换到低维空间
X_transformed = isomap.fit_transform(X)
```
