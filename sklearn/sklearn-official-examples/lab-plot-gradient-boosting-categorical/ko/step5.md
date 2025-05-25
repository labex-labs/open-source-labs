# 기본 범주형 지원 파이프라인

HistGradientBoostingRegressor 추정기의 기본 범주형 지원 기능을 활용하여 범주형 특징을 처리하는 파이프라인을 생성합니다. 여전히 OrdinalEncoder 를 사용하여 데이터를 사전 처리합니다.

```python
hist_native = make_pipeline(
    ordinal_encoder,
    HistGradientBoostingRegressor(
        random_state=42,
        categorical_features=categorical_columns,
    ),
).set_output(transform="pandas")
```
