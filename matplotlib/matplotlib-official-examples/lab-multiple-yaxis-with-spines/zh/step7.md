# 设置刻度颜色

我们将每个 y 轴的刻度颜色设置为与标签颜色匹配。

```python
ax.tick_params(axis='y', colors=p1.get_color())
twin1.tick_params(axis='y', colors=p2.get_color())
twin2.tick_params(axis='y', colors=p3.get_color())
```
