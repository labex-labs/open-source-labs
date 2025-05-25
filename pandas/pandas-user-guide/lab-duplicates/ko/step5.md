# 중복 레이블 허용 금지

필요한 경우, `set_flags(allows_duplicate_labels=False)` 메서드를 사용하여 중복 레이블을 허용하지 않도록 설정할 수 있습니다.

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
