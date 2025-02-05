# 在拟合后配置`transform`

可以在`fit`之后调用`set_output`，以便事后配置`transform`。

```python
scaler2 = StandardScaler()

scaler2.fit(X_train)
X_test_np = scaler2.transform(X_test)
print(f"默认输出类型: {type(X_test_np).__name__}")

scaler2.set_output(transform="pandas")
X_test_df = scaler2.transform(X_test)
print(f"配置后的pandas输出类型: {type(X_test_df).__name__}")
```
