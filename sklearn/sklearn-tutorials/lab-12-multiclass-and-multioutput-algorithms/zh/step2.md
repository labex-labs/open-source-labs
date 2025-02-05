# 多标签分类

## 问题描述

多标签分类是一种分类任务，其中每个样本可以被分配多个标签。每个样本可以拥有的标签数量大于两个。

## 目标格式

多标签目标的有效表示形式是一个二进制矩阵，其中每行代表一个样本，每列代表一个类别。值为 1 表示样本中存在该标签，而 0 或 -1 表示不存在。

## 示例

让我们使用 make_classification 函数创建一个多标签分类问题：

```python
from sklearn.datasets import make_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier

# 生成一个多标签分类问题
X, y = make_classification(n_samples=100, n_features=10, n_informative=5, random_state=0)
y = y.reshape(-1, 1)

# 拟合一个多输出随机森林分类器
model = MultiOutputClassifier(RandomForestClassifier())
model.fit(X, y)

# 进行预测
predictions = model.predict(X)
print(predictions)
```
