# 전처리기 정의

이 단계에서는 데이터를 전처리하는 데 사용될 `ColumnTransformer`를 정의합니다.

```python
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ]
)
```
