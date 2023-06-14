# Perform the grid search

In this step, we will use the GridSearchCV function to perform the grid search. We will be searching for the best hyperparameters for the min_samples_split parameter of the DecisionTreeClassifier model.

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


