# Entraîner un classifieur d'arbre de décision

Tout d'abord, nous devons ajuster un classifieur d'arbre de décision en utilisant le jeu de données `load_iris` de scikit-learn. Ce jeu de données contient 3 classes de 50 instances chacune, où chaque classe fait référence à un type de plante d'iris. Nous allons diviser le jeu de données en ensembles d'entraînement et de test et ajuster un classifieur d'arbre de décision avec un maximum de 3 nœuds terminaux.

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
