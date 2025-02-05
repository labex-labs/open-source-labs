# 生成直方图数据

既然我们已经有了随机数据，就可以使用numpy生成直方图了。我们将使用50个 bins 来创建直方图。添加以下代码：

```python
n, bins = np.histogram(data, 50)
```
