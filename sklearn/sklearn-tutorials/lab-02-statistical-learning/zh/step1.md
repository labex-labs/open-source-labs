# 理解数据集

Scikit-learn将数据集表示为二维数组，其中第一轴表示样本，第二轴表示特征。让我们通过鸢尾花数据集来看一个例子：

```python
from sklearn import datasets

iris = datasets.load_iris()
data = iris.data
print(data.shape)
```

输出：

```
(150, 4)
```

鸢尾花数据集由150个鸢尾花观测值组成，每个观测值由4个特征描述。数据数组的形状是(150, 4)。
