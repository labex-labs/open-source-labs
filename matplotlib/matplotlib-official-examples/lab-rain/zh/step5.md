# 创建动画

最后，我们将使用 `FuncAnimation` 对象创建动画，传入图形、更新函数、帧之间的时间间隔（以毫秒为单位）以及要保存的帧数。

```python
animation = FuncAnimation(fig, update, interval=10, save_count=100)
plt.show()
```
