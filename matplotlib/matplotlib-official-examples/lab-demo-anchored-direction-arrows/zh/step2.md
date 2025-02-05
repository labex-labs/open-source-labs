# 创建一个绘图

接下来，我们将使用NumPy创建一个简单的绘图。这个绘图将作为带锚定方向箭头的背景。

```python
# 为了可重复性固定随机状态
np.random.seed(19680801)

fig, ax = plt.subplots()
ax.imshow(np.random.random((10, 10)))
```
