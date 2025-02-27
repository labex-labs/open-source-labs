# Imputación iterativa de valores faltantes

Otra opción es IterativeImputer. Esto utiliza regresión lineal en un ciclo, modelando cada característica con valores faltantes como una función de otras características, sucesivamente. La versión implementada asume variables Gaussianas (de salida). Si tus características son obviamente no normales, considera transformarlas para que se vean más normales con el fin de potencialmente mejorar el rendimiento.

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
