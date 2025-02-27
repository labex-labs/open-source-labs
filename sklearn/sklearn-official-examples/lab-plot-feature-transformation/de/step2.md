# Training Ensemble Methods

Für jede der Ensemble-Methoden werden wir 10 Schätzer und eine maximale Tiefe von 3 Ebenen verwenden.

```python
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

n_estimators = 10
max_depth = 3

random_forest = RandomForestClassifier(
    n_estimators=n_estimators, max_depth=max_depth, random_state=10
)
random_forest.fit(X_train_ensemble, y_train_ensemble)

gradient_boosting = GradientBoostingClassifier(
    n_estimators=n_estimators, max_depth=max_depth, random_state=10
)
_ = gradient_boosting.fit(X_train_ensemble, y_train_ensemble)
```
