# 从全名中提取姓氏

现在，让我们创建一个新列“Surname”，其中包含乘客的姓氏。我们将通过提取“Name”列中逗号之前的部分来实现这一点。

```python
# 在逗号处拆分“Name”列并提取第一部分
titanic["Surname"] = titanic["Name"].str.split(",").str.get(0)
```
