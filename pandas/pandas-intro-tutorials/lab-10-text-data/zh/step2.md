# 将字符串字符转换为小写

接下来，我们将把“Name”列中的所有字符转换为小写。我们将使用`str.lower()`方法来实现这一点。

```python
# 将“Name”列中的所有字符转换为小写
titanic["Name"] = titanic["Name"].str.lower()
```
