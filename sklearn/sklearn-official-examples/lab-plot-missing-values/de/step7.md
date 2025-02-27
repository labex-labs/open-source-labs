# Iterative Einschätzung der fehlenden Werte

Eine weitere Option ist der IterativeImputer. Dieser verwendet eine Rund-Robin-Linear-Regression, um jeweils jede Feature mit fehlenden Werten als Funktion der anderen Feature zu modellieren. Die implementierte Version nimmt an, dass die Variablen (Output) gaussian verteilt sind. Wenn Ihre Feature offensichtlich nicht normal verteilt sind, sollten Sie sie möglicherweise transformieren, um sie normaler zu gestalten und so eventuell die Leistung zu verbessern.

```python
def get_impute_iterative(X_missing, y_missing):
    imputer = IterativeImputer(
        missing_values=np.nan,
        add_indicator=True,
        random_state=0,
        n_nearest_features=3,
        max_iter=1,
        sample_posterior=True,
    )
    iterative_impute_scores = get_scores_for_imputer(imputer, X_missing, y_missing)
    return iterative_impute_scores.mean(), iterative_impute_scores.std()

mses_california[4], stds_california[4] = get_impute_iterative(
    X_miss_california, y_miss_california
)
mses_diabetes[4], stds_diabetes[4] = get_impute_iterative(
    X_miss_diabetes, y_miss_diabetes
)
x_labels.append("Iterative Imputation")

mses_diabetes = mses_diabetes * -1
mses_california = mses_california * -1
```
