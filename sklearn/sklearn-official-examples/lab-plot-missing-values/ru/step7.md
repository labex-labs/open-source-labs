# Итеративное заполнение пропущенных значений

Другой вариант - это IterativeImputer. Он использует линейную регрессию по кругу, моделируя каждую характеристику с пропущенными значениями как функцию других характеристик, по очереди. Реализованная версия предполагает гауссовские (выходные) переменные. Если ваши характеристики явно не являются нормальными, рассмотрите их преобразование, чтобы они выглядели более нормальными, чтобы потенциально повысить производительность.

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
