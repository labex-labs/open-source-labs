# 为图表添加标签和标题

最后一步是为图表添加标签和标题。我们将为图表添加一个标题、一个 x 轴标签以及图表的图例。

```python
ax.set_title('Cup height by group and beverage choice')
ax.set_xlabel('Group')
ax.legend()
ax.autoscale_view()
```
