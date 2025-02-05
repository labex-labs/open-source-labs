# 索引中的重复项

接下来，我们将探讨索引中的重复项如何导致意外结果。

```python
# 创建一个具有重复列标签的DataFrame
df1 = pd.DataFrame([[0, 1, 2], [3, 4, 5]], columns=["A", "A", "B"])

# 索引'B'返回一个Series
print(df1["B"])

# 索引'A'返回一个DataFrame
print(df1["A"])
```
