# 提取特定乘客数据

接下来，让我们提取泰坦尼克号上伯爵夫人的乘客数据。我们将使用`str.contains()`方法来查找“Name”列中包含“Countess”一词的行。

```python
# 查找“Name”列中包含“Countess”的行
countesses = titanic[titanic["Name"].str.contains("Countess")]
```
