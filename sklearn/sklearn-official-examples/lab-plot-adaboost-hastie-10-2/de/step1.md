# Daten und Baselinemodelle vorbereiten

Wir beginnen mit der Erzeugung des binären Klassifizierungsdatensatzes, der in Hastie et al. 2009, Beispiel 10.2, verwendet wird. Anschließend legen wir die Hyperparameter für unsere AdaBoost-Klassifizierer fest. Wir teilen die Daten in einen Trainings- und einen Testsatz auf. Danach trainieren wir unsere Baselinemodelle, einen `DecisionTreeClassifier` mit `depth=9` und einen "Stumpf" `DecisionTreeClassifier` mit `depth=1`, und berechnen den Testfehler.

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
