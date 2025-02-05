# 设置绘图

我们创建一个新的图形和轴对象，并初始化 Scope 类。然后，我们将更新函数和发射器函数传递给 FuncAnimation 方法以创建动画。

```python
fig, ax = plt.subplots()
scope = Scope(ax)

ani = animation.FuncAnimation(fig, scope.update, emitter, interval=50,
                              blit=True, save_count=100)

plt.show()
```
