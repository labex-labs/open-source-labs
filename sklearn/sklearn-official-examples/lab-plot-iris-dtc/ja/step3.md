# 決定木の構造を表示する

次に、アイリスのデータセットのすべての特徴量で学習された単一の決定木の構造を表示します。

```python
from sklearn.tree import plot_tree

plt.figure()
clf = DecisionTreeClassifier().fit(iris.data, iris.target)
plot_tree(clf, filled=True)
plt.title("Decision tree trained on all the iris features")
plt.show()
```
