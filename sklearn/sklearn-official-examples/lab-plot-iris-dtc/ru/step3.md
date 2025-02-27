# Отображение структуры дерева решений

Далее мы отобразим структуру одного дерева решений, обученного на всех признаках датасета Iris.

```python
from sklearn.tree import plot_tree

plt.figure()
clf = DecisionTreeClassifier().fit(iris.data, iris.target)
plot_tree(clf, filled=True)
plt.title("Decision tree trained on all the iris features")
plt.show()
```
