# 欠損値の反復補完

もう一つのオプションは IterativeImputer です。これは、循環的な線形回帰を使用して、欠損値を持つ各特徴量を他の特徴量の関数として順番にモデル化します。実装されているバージョンはガウス型（出力）変数を想定しています。特徴量が明らかに非正規分布の場合、性能を向上させるために、より正規分布に近いように変換することを検討してください。

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
