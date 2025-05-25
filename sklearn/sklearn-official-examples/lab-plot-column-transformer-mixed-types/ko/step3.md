# 숫자형 및 범주형 특징 정의

이 단계에서는 파이프라인에 사용할 숫자형 및 범주형 특징을 정의합니다. 또한 숫자형 및 범주형 데이터에 대한 전처리 파이프라인을 정의합니다.

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
