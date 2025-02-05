# 选择特定的行和列

要一次性选择行和列，我们使用 `loc` 或 `iloc` 运算符。

```python
# 选择年龄大于35岁乘客的 'Name'
adult_names = titanic.loc[titanic["Age"] > 35, "Name"]

# 显示前5行
adult_names.head()
```
