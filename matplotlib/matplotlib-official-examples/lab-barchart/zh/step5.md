# 自定义图表

我们可以通过添加标签、标题，调整x轴刻度标签和图例来定制图表。我们还将设置y轴限制，以确保所有数据都可见。

```python
ax.set_ylabel('Length (mm)')
ax.set_title('Penguin attributes by species')
ax.set_xticks(x + width, species)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 250)
```
