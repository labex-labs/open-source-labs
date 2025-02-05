# 验证

为了验证逆变换的正确性，我们可以将原始数据 `X` 与逆变换的结果进行比较。

```python
X_new_again = transformer.transform(X_new_inversed)
np.allclose(X_new, X_new_again)
```

在这里，我们将变换应用于逆变换后的数据 `X_new_inversed`，并使用 `np.allclose` 函数检查它是否等于原始的投影数据 `X_new`。
