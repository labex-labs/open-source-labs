# 数値型とカテゴリ型の特徴量を定義する

このステップでは、パイプラインで使用する数値型とカテゴリ型の特徴量を定義します。また、数値型とカテゴリ型のデータの前処理パイプラインも定義します。

```python
numeric_features = ["age", "fare"]
numeric_transformer = Pipeline(
    steps=[("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]
)

categorical_features = ["embarked", "sex", "pclass"]
categorical_transformer = Pipeline(
    steps=[
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
        ("selector", SelectPercentile(chi2, percentile=50)),
    ]
)
```
