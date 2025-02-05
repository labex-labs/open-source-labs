# 创建图表

接下来，让我们使用`imshow`和由`numpy.random`生成的随机数组创建两个图表。我们还将为图表添加一个颜色条。运行以下代码：

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

plt.subplot(211)
plt.imshow(np.random.random((100, 100)))
plt.subplot(212)
plt.imshow(np.random.random((100, 100)))

cax = plt.axes([0.85, 0.1, 0.075, 0.8])
plt.colorbar(cax=cax)

plt.show()
```
