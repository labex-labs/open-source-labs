# 创建条形图

接下来，我们创建堆积条形图。我们首先定义图表的参数：

```python
# 条形图参数
bottom = 1
width =.2

# 从顶部添加与图例匹配。
for j, (height, label) in enumerate(reversed([*zip(age_ratios, age_labels)])):
    bottom -= height
    bc = ax2.bar(0, height, width, bottom=bottom, color='C0', label=label,
                 alpha=0.1 + 0.25 * j)
    ax2.bar_label(bc, labels=[f"{height:.0%}"], label_type='center')
```
