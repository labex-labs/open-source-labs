# Определение числовых и категориальных признаков

В этом шаге мы определим числовые и категориальные признаки, которые будем использовать в нашем конвейере. Также мы определим конвейеры предварительной обработки как для числовых, так и для категориальных данных.

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
