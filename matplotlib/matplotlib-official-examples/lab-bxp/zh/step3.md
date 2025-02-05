# 自定义箱线图统计量

我们可以修改在步骤2中计算出的任何箱线图统计量。在这个例子中，我们将每组数据的中位数设置为所有数据的中位数，并将均值翻倍。

```python
for n in range(len(stats)):
    stats[n]['med'] = np.median(data)
    stats[n]['mean'] *= 2
```
