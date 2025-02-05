# 对数据进行排序

为了绘制出平滑的曲线，我们将使用 `sort()` 方法对数据进行排序。

```python
# split the data into two parts
xdata1 = xdata[0, :]
xdata2 = xdata[1, :]
# sort the data so it makes clean curves
xdata1.sort()
xdata2.sort()
```
