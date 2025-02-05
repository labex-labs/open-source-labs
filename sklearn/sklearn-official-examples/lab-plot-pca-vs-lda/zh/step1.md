# 加载数据集

首先，我们需要使用scikit-learn的内置函数`load_iris()`来加载鸢尾花数据集。

```python
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()

X = iris.data
y = iris.target
target_names = iris.target_names
```
