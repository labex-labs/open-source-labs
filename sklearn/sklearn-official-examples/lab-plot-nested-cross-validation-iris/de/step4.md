# Nicht-geschachtelte Kreuzvalidierung (Non-Nested Cross-Validation)

Wir verwenden nicht-geschachtelte Kreuzvalidierung, um die Hyperparameter zu optimieren und die Leistung des Modells zu bewerten. Die Funktion `GridSearchCV` führt eine erschöpfende Suche über die angegebenen Parameterwerte für einen Schätzer (estimator) durch. Wir verwenden eine 4-fache Kreuzvalidierung.

```python
from sklearn.model_selection import GridSearchCV

# Non_nested parameter search and scoring
clf = GridSearchCV(estimator=svm, param_grid=p_grid, cv=4)
clf.fit(X_iris, y_iris)
non_nested_score = clf.best_score_
```
