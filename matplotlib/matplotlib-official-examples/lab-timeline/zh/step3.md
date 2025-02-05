# 格式化图表

现在，我们将通过添加 x 轴和 y 轴标签、设置 x 轴主定位器和格式化器以及移除 y 轴和脊柱来格式化图表。以下是格式化图表的代码：

```python
# 以 4 个月为间隔格式化 x 轴
ax.xaxis.set_major_locator(mdates.MonthLocator(interval = 4))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
plt.setp(ax.get_xticklabels(), rotation = 30, ha = "right")

# 移除 y 轴和脊柱
ax.yaxis.set_visible(False)
ax.spines[["left", "top", "right"]].set_visible(False)

ax.margins(y = 0.1)
plt.show()
```
