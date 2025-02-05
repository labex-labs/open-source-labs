# 展示决策树结构

接下来，我们将展示在鸢尾花数据集的所有特征上训练的单个决策树的结构。

```python
from sklearn.tree import plot_tree

plt.figure()
clf = DecisionTreeClassifier().fit(iris.data, iris.target)
plot_tree(clf, filled=True)
plt.title("Decision tree trained on all the iris features")
plt.show()
```
