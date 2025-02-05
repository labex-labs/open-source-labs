# 顶部标题

使用`subplots()`函数和`set_xlabel()`函数创建一个标题位于顶部的图表。

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.xaxis.set_label_position('top')
ax.set_xlabel('X-label')
ax.set_title('Top Title')
```
