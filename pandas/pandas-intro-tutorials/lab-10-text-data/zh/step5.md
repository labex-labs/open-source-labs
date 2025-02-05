# 找出最长的名字

让我们找出泰坦尼克号上名字最长的乘客。我们将使用`str.len()`方法来获取每个名字的长度，并使用`idxmax()`方法来找到最长名字的索引。

```python
# 获取每个名字的长度
name_lengths = titanic["Name"].str.len()

# 找到最长名字的索引
longest_name_index = name_lengths.idxmax()

# 获取最长的名字
longest_name = titanic.loc[longest_name_index, "Name"]
```
