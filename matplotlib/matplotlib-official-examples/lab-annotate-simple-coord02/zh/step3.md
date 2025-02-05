# 添加箭头注释

箭头可用于指出图表中的特定特征或趋势。在这一步中，我们将向图表添加一个指向最大值的箭头。

```python
# 找到最大值
y = [0, 1, 4, 9, 16]
max_index = y.index(max(y))
xmax = max_index
ymax = y[max_index]

# 添加箭头注释
ax.annotate('Maximum Value', xy=(xmax, ymax), xytext=(xmax, ymax + 5),
            arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()
```
