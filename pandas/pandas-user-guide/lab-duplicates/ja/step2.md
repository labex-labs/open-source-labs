# 重複ラベルの影響を理解する

重複ラベルは、pandas の特定の操作の動作を変更する可能性があります。たとえば、重複が存在する場合、一部のメソッドは機能しません。

```python
# Creating a pandas Series with duplicate labels
s1 = pd.Series([0, 1, 2], index=["a", "b", "b"])

# Attempting to reindex the Series
try:
    s1.reindex(["a", "b", "c"])
except Exception as e:
    print(e)
```
