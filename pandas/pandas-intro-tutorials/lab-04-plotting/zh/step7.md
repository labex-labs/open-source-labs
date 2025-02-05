# 为每列创建子图

我们可以使用 `subplots` 参数为每个数据列创建单独的子图。

```python
# 为每列创建子图
axs = air_quality.plot.area(figsize=(12, 4), subplots=True)
plt.show()
```
