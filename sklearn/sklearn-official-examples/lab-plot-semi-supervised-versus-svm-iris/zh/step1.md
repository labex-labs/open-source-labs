# 加载鸢尾花数据集并划分数据

我们将加载鸢尾花数据集，这是机器学习中广泛用于分类任务的数据集。该数据集包含150个鸢尾花样本，每个样本有四个特征：萼片长度、萼片宽度、花瓣长度和花瓣宽度。我们将把数据集划分为输入特征和目标标签。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

# 加载鸢尾花数据集
iris = datasets.load_iris()

# 将数据集划分为输入特征和目标标签
X = iris.data[:, :2] # 为了可视化目的，我们仅使用前两个特征
y = iris.target
```
