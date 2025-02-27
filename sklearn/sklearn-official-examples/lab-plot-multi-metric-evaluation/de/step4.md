# Das Gitter-Search ausführen

In diesem Schritt verwenden wir die GridSearchCV-Funktion, um das Gitter-Search durchzuführen. Wir suchen die besten Hyperparameter für den min_samples_split-Parameter des DecisionTreeClassifier-Modells.

```python
gs = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    param_grid={"min_samples_split": range(2, 403, 20)},
    scoring=scoring,
    refit="AUC",
    n_jobs=2,
    return_train_score=True,
)
gs.fit(X, y)
results = gs.cv_results_
```
