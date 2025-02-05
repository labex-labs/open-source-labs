# 准备数据和基线模型

我们首先生成Hastie等人2009年示例10.2中使用的二元分类数据集。然后，我们为AdaBoost分类器设置超参数。我们将数据拆分为训练集和测试集。之后，我们训练基线分类器，一个深度为9的`DecisionTreeClassifier`和一个深度为1的“树桩”`DecisionTreeClassifier`，并计算测试误差。

```python
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X, y = datasets.make_hastie_10_2(n_samples=12_000, random_state=1)

n_estimators = 400
learning_rate = 1.0

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=2_000, shuffle=False
)

dt_stump = DecisionTreeClassifier(max_depth=1, min_samples_leaf=1)
dt_stump.fit(X_train, y_train)
dt_stump_err = 1.0 - dt_stump.score(X_test, y_test)

dt = DecisionTreeClassifier(max_depth=9, min_samples_leaf=1)
dt.fit(X_train, y_train)
dt_err = 1.0 - dt.score(X_test, y_test)
```
