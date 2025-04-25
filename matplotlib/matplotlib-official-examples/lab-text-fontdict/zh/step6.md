# 自定义坐标轴标签

我们也可以使用字体字典来自定义绘图的坐标轴标签。我们将把 xlabel() 和 ylabel() 函数的 fontdict 参数设置为我们的字体字典。

```python
plt.xlabel('Time (s)', fontdict=font)
plt.ylabel('Voltage (mV)', fontdict=font)
```
