# 加载鸢尾花数据集

我们将从 scikit-learn 库中加载鸢尾花数据集。该数据集包含四个特征：萼片长度、萼片宽度、花瓣长度和花瓣宽度。我们将仅使用前两个特征进行二元分类。

```python
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
y = iris.target

X = X[y!= 2] # 仅使用前两个特征进行二元分类
y = y[y!= 2]

X /= X.max() # 对 X 进行归一化以加速收敛
```
