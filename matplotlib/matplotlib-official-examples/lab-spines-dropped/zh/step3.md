# 创建图形和坐标轴

我们将使用 `plt.subplots()` 创建一个图形和一个坐标轴对象。`imshow()` 函数用于将随机数据显示为图像。

```python
fig, ax = plt.subplots()

image = np.random.uniform(size=(10, 10))
ax.imshow(image, cmap=plt.cm.gray)
ax.set_title('dropped spines')
```
