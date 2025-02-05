# 自定义坐标轴标签

我们也可以使用字体字典来自定义绘图的坐标轴标签。我们将把xlabel()和ylabel()函数的fontdict参数设置为我们的字体字典。

```python
plt.xlabel('Time (s)', fontdict=font)
plt.ylabel('Voltage (mV)', fontdict=font)
```
