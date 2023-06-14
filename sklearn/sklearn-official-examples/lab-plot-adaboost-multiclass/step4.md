# Create and Train the Models

We will create two AdaBoost models, one using SAMME and the other using SAMME.R. Both models will use DecisionTreeClassifier with a max depth of 2 and 300 estimators.

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


