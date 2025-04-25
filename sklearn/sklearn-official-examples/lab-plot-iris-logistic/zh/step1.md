# 加载数据集并进行预处理

我们将使用 scikit-learn 库来加载鸢尾花数据集。该数据集包含 3 个类别，每个类别有 50 个实例，每个类别代表一种鸢尾属植物。每个实例有 4 个特征：萼片长度、萼片宽度、花瓣长度和花瓣宽度。

```python
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.inspection import DecisionBoundaryDisplay

# 加载鸢尾花数据集
iris = datasets.load_iris()
X = iris.data[:, :2]  # 我们只取前两个特征。
Y = iris.target
```
