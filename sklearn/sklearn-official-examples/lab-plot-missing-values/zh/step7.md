# 缺失值的迭代插补

另一种选择是迭代插补器（IterativeImputer）。它使用循环线性回归，依次将每个具有缺失值的特征建模为其他特征的函数。所实现的版本假设变量为高斯分布（输出）。如果你的特征明显非正态，考虑对它们进行变换，使其看起来更接近正态分布，这可能会提高性能。

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
