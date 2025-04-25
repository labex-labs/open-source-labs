# 在子图上绘制一些内容

我们将在子图上绘制一些内容，以便用户可以看到矩形选择器（RectangleSelector）和椭圆选择器（EllipseSelector）的效果。

```python
N = 100000  # 如果 N 很大，使用双缓冲（blitting）可以看到性能提升。
x = np.linspace(0, 10, N)

for ax in axs:
    ax.plot(x, np.sin(2*np.pi*x))  # 绘制一些内容
```
