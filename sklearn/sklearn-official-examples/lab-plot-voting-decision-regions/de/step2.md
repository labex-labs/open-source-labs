# Klassifizierer trainieren

Wir werden drei Klassifizierer initialisieren: `DecisionTreeClassifier`, `KNeighborsClassifier` und `SVC`. Anschließend werden wir einen `VotingClassifier` mit diesen drei Klassifizierern initialisieren und ihn verwenden, um die Klasse der Iris-Blumen vorherzusagen.

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier

clf1 = DecisionTreeClassifier(max_depth=4)
clf2 = KNeighborsClassifier(n_neighbors=7)
clf3 = SVC(gamma=0.1, kernel="rbf", probability=True)

eclf = VotingClassifier(
    estimators=[("dt", clf1), ("knn", clf2), ("svc", clf3)],
    voting="soft",
    weights=[2, 1, 2],
)

clf1.fit(X, y)
clf2.fit(X, y)
clf3.fit(X, y)
eclf.fit(X, y)
```
