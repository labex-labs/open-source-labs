# 创建简单误差线图

我们将使用`errorbar`函数创建一个带有标准误差线的简单误差线图。在这里，我们将设置x和y值以及它们相应的误差值。我们还将把线条样式设置为虚线。

```python
fig, ax = plt.subplots(figsize=(7, 4))

# 标准误差线
ax.errorbar(x, y, xerr=xerr, yerr=yerr, linestyle='dotted')
```
