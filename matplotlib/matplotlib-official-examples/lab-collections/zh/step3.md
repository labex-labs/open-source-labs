# 创建偏移量

```python
# 为保证可重复性而固定随机状态
rs = np.random.RandomState(19680801)

# 生成一些偏移量
xyo = rs.randn(npts, 2)
```

第三步是使用Numpy创建偏移量。我们将使用随机函数来创建偏移量。
