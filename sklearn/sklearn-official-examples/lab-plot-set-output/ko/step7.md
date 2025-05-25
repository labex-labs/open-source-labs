# `config_context`를 사용하여 `set_output` 설정

`config_context`를 사용하여 출력 형식을 설정할 때, `transform` 또는 `fit_transform`가 호출되는 시점의 설정이 적용됩니다.

```python
scaler = StandardScaler()
scaler.fit(X_train[num_cols])

with config_context(transform_output="pandas"):
    X_test_scaled = scaler.transform(X_test[num_cols])
X_test_scaled.head()
```
