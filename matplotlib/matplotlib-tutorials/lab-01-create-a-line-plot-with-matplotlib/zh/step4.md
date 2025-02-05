# 自定义图表

我们可以通过为x轴和y轴添加标签、为图表添加标题以及添加图例来定制图表。我们还可以更改线条样式和颜色。

```python
plt.plot(x, y, linestyle='--', color='red', label='sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line Plot')
plt.legend()
```
