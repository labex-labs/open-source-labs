# 多类-多输出分类

## 问题描述

多类-多输出分类，也称为多任务分类，为每个样本预测多个非二元属性。每个属性可以有两个以上的类别。

## 目标格式

多类-多输出目标的有效表示形式是一个密集矩阵，其中每行代表一个样本，每列代表一个不同的属性或类别。

## 示例

让我们使用 make_classification 函数创建一个多类-多输出分类问题：

```python
from sklearn.datasets import make_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.svm import SVC

# 生成一个多类-多输出分类问题
X, y = make_classification(n_samples=100, n_features=10, n_informative=5, n_classes=3, random_state=0)

# 拟合一个多输出支持向量分类器
model = MultiOutputClassifier(SVC())
model.fit(X, y)

# 进行预测
predictions = model.predict(X)
print(predictions)
```
