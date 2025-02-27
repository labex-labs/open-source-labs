# Modelle definieren

In diesem Schritt definieren wir die Modelle, die zur Darstellung der Entscheidungsflächen auf dem Iris-Datensatz verwendet werden sollen.

```python
models = [
    DecisionTreeClassifier(max_depth=None),
    RandomForestClassifier(n_estimators=n_estimators),
    ExtraTreesClassifier(n_estimators=n_estimators),
    AdaBoostClassifier(DecisionTreeClassifier(max_depth=3), n_estimators=n_estimators),
]
```
