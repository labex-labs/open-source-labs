# 自定义图表

我们可以通过为 x 轴和 y 轴添加标签，并将 y 轴的刻度设置为对数，来自定义图表的外观。

```python
ax.set_xticks(x + dimw / 2, labels=map(str, x))
ax.set_yscale('log')

ax.set_xlabel('x')
ax.set_ylabel('y')
```
