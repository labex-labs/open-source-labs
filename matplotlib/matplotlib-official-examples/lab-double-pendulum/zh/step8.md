# 创建动画

现在我们将使用Matplotlib中的FuncAnimation函数来创建动画。

```python
ani = animation.FuncAnimation(
    fig, animate, len(y), interval=dt*1000, blit=True)
plt.show()
```
