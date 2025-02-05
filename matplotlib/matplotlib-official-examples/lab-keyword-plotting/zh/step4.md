# 生成图表

在这一步中，我们将使用`data`字典作为`scatter()`函数的输入来生成散点图。我们将使用与`a`、`b`、`c`和`d`变量相对应的字符串来生成图表。

```python
fig, ax = plt.subplots()
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set(xlabel='entry a', ylabel='entry b')
plt.show()
```
