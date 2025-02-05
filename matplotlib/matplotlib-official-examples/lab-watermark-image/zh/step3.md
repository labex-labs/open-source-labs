# 创建绘图

现在，我们可以创建要在其上叠加图像的绘图了。在这个例子中，我们将使用随机数据创建一个简单的条形图。

```python
fig, ax = plt.subplots()

np.random.seed(19680801)
x = np.arange(30)
y = x + np.random.randn(30)
ax.bar(x, y, color='#6bbc6b')
ax.grid()
```
