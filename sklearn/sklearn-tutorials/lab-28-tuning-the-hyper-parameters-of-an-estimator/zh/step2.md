# 加载数据集

接下来，让我们加载要使用的数据集。在本练习中，我们可以使用任何我们选择的数据集。

```python
from sklearn.datasets import load_iris

# 加载鸢尾花数据集
iris = load_iris()

# 将数据拆分为特征和目标
X = iris.data
y = iris.target
```
