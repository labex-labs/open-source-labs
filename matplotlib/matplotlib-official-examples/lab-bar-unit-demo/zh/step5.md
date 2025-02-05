# 创建柱状图

下一步是创建柱状图。我们将使用`bar()`函数来创建图表。我们将创建两组柱子，一组代表茶，一组代表咖啡。我们还将为图表添加误差线。

```python
ax.bar(ind, tea_means, width, bottom=0*cm, yerr=tea_std, label='Tea')
ax.bar(ind + width, coffee_means, width, bottom=0*cm, yerr=coffee_std,
       label='Coffee')
```
