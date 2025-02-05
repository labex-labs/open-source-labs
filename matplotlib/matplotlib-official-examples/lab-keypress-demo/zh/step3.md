# 创建绘图并连接按键事件监听器

我们使用 `np.random.rand()` 生成随机数据来创建一个简单的绘图。然后，我们使用 `fig.canvas.mpl_connect()` 设置按键事件监听器，并传入我们想要监听的事件名称（`'key_press_event'`）以及事件发生时要调用的函数（`on_press`）。

```python
fig, ax = plt.subplots()

fig.canvas.mpl_connect('key_press_event', on_press)

ax.plot(np.random.rand(12), np.random.rand(12), 'go')
xl = ax.set_xlabel('easy come, easy go')
ax.set_title('Press a key')
plt.show()
```
