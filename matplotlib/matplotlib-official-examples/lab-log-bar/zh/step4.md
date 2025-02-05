# 自定义图表

我们可以通过为x轴和y轴添加标签，并将y轴的刻度设置为对数，来自定义图表的外观。

```python
ax.set_xticks(x + dimw / 2, labels=map(str, x))
ax.set_yscale('log')

ax.set_xlabel('x')
ax.set_ylabel('y')
```
