# 使用可调用对象进行柱状图标注

最后，我们将展示如何使用可调用对象来格式化柱状图标签。我们将使用一些不同动物奔跑速度的数据。

```python
动物名称 = ['狮子', '瞪羚', '猎豹']
英里每小时速度 = [50, 60, 75]

fig, ax = plt.subplots()
柱状图容器 = ax.bar(动物名称, 英里每小时速度)
ax.set(ylabel='英里每小时速度', title='奔跑速度', ylim=(0, 80))
ax.bar_label(柱状图容器, fmt=lambda x: f'{x * 1.61:.1f} 公里/小时')
```
