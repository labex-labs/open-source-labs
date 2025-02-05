# 加载数据

我们将使用 Scikit-Learn 的 `datasets` 模块加载鸢尾花数据集。我们只使用两个特征：萼片长度和花瓣长度。

```python
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data[:, [0, 2]]
y = iris.target
```
