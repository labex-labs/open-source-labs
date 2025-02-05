# 训练决策树分类器

首先，我们需要使用scikit-learn中的`load_iris`数据集来拟合一个决策树分类器。这个数据集包含3个类别，每个类别有50个实例，每个类别代表一种鸢尾花植物。我们将把数据集拆分为训练集和测试集，并拟合一个最多有3个叶节点的决策树分类器。

```python
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

clf = DecisionTreeClassifier(max_leaf_nodes=3, random_state=0)
clf.fit(X_train, y_train)
```
