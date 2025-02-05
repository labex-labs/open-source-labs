# 理解重复标签的影响

重复标签可能会改变pandas中某些操作的行为。例如，当存在重复项时，一些方法将无法正常工作。

```python
# 创建一个带有重复标签的pandas Series
s1 = pd.Series([0, 1, 2], index=["a", "b", "b"])

# 尝试对Series进行重新索引
try:
    s1.reindex(["a", "b", "c"])
except Exception as e:
    print(e)
```
