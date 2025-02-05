# 在 Pandas 中使用 if/真值语句

由于存在歧义，Pandas 不支持直接使用 if/真值语句。相反，请使用 `.any()`、`.all()` 或 `.empty()` 等方法。

```python
# 检查 Series 中是否有任何值为 True
if pd.Series([False, True, False]).any():
    print("At least one True value in the Series")
```
