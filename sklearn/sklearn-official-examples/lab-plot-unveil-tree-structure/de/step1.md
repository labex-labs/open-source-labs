# Ein Entscheidungsbaum-Klassifizierer trainieren

Zunächst müssen wir einen Entscheidungsbaum-Klassifizierer mit dem `load_iris`-Datensatz aus scikit-learn anpassen. Dieser Datensatz enthält 3 Klassen mit jeweils 50 Instanzen, wobei jede Klasse auf eine Art von Iris-Pflanze Bezug nimmt. Wir werden den Datensatz in Trainings- und Testsets unterteilen und einen Entscheidungsbaum-Klassifizierer mit maximal 3 Blättern anpassen.

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
