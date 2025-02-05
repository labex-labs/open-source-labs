# 创建散点图

我们将使用随机数据点创建一个散点图。

```python
# 为保证可重复性而固定随机状态
np.random.seed(19680801)

# 创建随机数据点
x, y = np.random.normal(size=(2, 200))

# 创建散点图
plt.plot(x, y, 'o')
plt.show()
```
