# Imputation itérative des valeurs manquantes

Une autre option est l'IterativeImputer. Cela utilise une régression linéaire en boucle, en modélisant chaque caractéristique avec des valeurs manquantes en fonction des autres caractéristiques, tour à tour. La version implémentée suppose des variables gaussiennes (de sortie). Si vos caractéristiques ne sont pas manifestement normales, envisagez de les transformer pour les rendre plus normales afin de potentiellement améliorer les performances.

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
