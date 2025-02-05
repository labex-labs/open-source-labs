# 创建图表

接下来，我们将通过定义宿主轴和寄生轴来创建图表。宿主轴将用于主数据，寄生轴将用于辅助数据。

```python
host = host_subplot(111)
par = host.twinx()
```
