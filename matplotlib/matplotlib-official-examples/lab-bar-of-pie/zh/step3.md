# 创建饼图

现在我们可以创建饼图了。我们首先定义图形和轴对象：

```python
# 生成图形并分配轴对象
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))
fig.subplots_adjust(wspace=0)
```

然后我们设置饼图的参数并绘制它：

```python
# 旋转以便第一个楔形被x轴分割
angle = -180 * overall_ratios[0]
wedges, *_ = ax1.pie(overall_ratios, autopct='%1.1f%%', startangle=angle,
                     labels=labels, explode=explode)
```
