# 重複ラベルの禁止

必要に応じて、`set_flags(allows_duplicate_labels=False)` メソッドを使用して重複ラベルを禁止することができます。

```python
# Disallowing duplicate labels in a Series
try:
    pd.Series([0, 1, 2], index=["a", "b", "b"]).set_flags(allows_duplicate_labels=False)
except Exception as e:
    print(e)

# Disallowing duplicate labels in a DataFrame
try:
    pd.DataFrame([[0, 1, 2], [3, 4, 5]], columns=["A", "B", "C"]).set_flags(allows_duplicate_labels=False)
except Exception as e:
    print(e)
```
