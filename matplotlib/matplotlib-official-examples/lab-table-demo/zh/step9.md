# 添加轴标签和标题

我们将使用`plt.ylabel`、`plt.yticks`、`plt.xticks`和`plt.title`函数为绘图添加轴标签和标题。

```python
values = np.arange(0, 2500, 500)
value_increment = 1000

plt.ylabel(f"Loss in ${value_increment}'s")
plt.yticks(values * value_increment, ['%d' % val for val in values])
plt.xticks([])
plt.title('Loss by Disaster')
```
