# `fit` 후 `transform` 설정

`set_output`는 `fit` 이후에 호출하여 사후에 `transform`을 설정할 수 있습니다.

```python
scaler2 = StandardScaler()

scaler2.fit(X_train)
X_test_np = scaler2.transform(X_test)
print(f"Default output type: {type(X_test_np).__name__}")

scaler2.set_output(transform="pandas")
X_test_df = scaler2.transform(X_test)
print(f"Configured pandas output type: {type(X_test_df).__name__}")
```
