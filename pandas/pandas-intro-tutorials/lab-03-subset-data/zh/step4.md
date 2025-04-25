# 筛选特定行

要根据条件表达式选择行，请在选择括号 `[]` 内使用该条件。

```python
# 筛选 'Age' 大于 35 的行
above_35 = titanic[titanic["Age"] > 35]

# 显示前 5 行
above_35.head()
```
