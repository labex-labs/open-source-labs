# Обучить классификатор дерева решений

Во - первых, нам нужно обучить классификатор дерева решений, используя датасет `load_iris` из scikit - learn. Этот датасет содержит 3 класса по 50 экземпляров каждый, где каждый класс относится к определенному типу ириса. Мы разделим датасет на обучающую и тестовую выборки и обучим классификатор дерева решений с максимальным количеством 3 листьев.

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
