# 多类分类

## 问题描述

多类分类是一种具有两个以上类别的分类任务。每个样本仅被分配到一个类别。

## 目标格式

多类目标的有效表示形式是一个一维或列向量，其中包含两个以上的离散值。

## 示例

让我们使用鸢尾花数据集来演示多类分类：

```python
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier

# 加载鸢尾花数据集
X, y = datasets.load_iris(return_X_y=True)

# 使用 OneVsRestClassifier 拟合逻辑回归模型
model = OneVsRestClassifier(LogisticRegression())
model.fit(X, y)

# 进行预测
predictions = model.predict(X)
print(predictions)
```
