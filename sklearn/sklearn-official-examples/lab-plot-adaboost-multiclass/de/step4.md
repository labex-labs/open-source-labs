# Erstellen und Trainieren der Modelle

Wir werden zwei AdaBoost-Modelle erstellen, eines mit SAMME und das andere mit SAMME.R. Beide Modelle werden DecisionTreeClassifier mit einer maximalen Tiefe von 2 und 300 Schätzern verwenden.

```python
bdt_real = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=2), n_estimators=300, learning_rate=1
)

bdt_discrete = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=2),
    n_estimators=300,
    learning_rate=1.5,
    algorithm="SAMME",
)

bdt_real.fit(X_train, y_train)
bdt_discrete.fit(X_train, y_train)
```
