# 创建子图

我们将创建三个子图来展示不同的脊柱（坐标轴框架）自定义设置。我们将使用紧凑布局来确保标签不会与坐标轴重叠。

```python
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, layout='constrained')
```
