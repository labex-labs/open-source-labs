# 创建分组柱状图

现在，我们可以使用 Matplotlib 的`bar`函数来创建图表。我们将创建一个循环，遍历我们的属性，并为每个属性创建一组柱子。我们还将调整柱子的宽度和每组柱子的位置。

```python
x = np.arange(len(species))
width = 0.25
multiplier = 0

fig, ax = plt.subplots()

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    multiplier += 1
```
