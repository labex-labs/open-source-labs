# Imputação Iterativa dos Valores Ausentes

Outra opção é o IterativeImputer. Este método utiliza regressão linear em rodízio, modelando cada característica com valores ausentes como uma função de outras características, por sua vez. A versão implementada assume variáveis gaussianas (de saída). Se as suas características forem obviamente não normais, considere transformá-las para parecerem mais normais, para potencialmente melhorar o desempenho.

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
x_labels.append("Imputação Iterativa")

mses_diabetes = mses_diabetes * -1
mses_california = mses_california * -1
```
