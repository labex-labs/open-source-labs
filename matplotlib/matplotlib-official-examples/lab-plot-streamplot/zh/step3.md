# 变化的密度

在这一步中，我们将创建一个具有变化密度的流线图。`density` 参数控制要绘制的流线数量。较高的值将导致更多的流线。

```python
plt.streamplot(X, Y, U, V, density=[0.5, 1])
plt.title('Varying Density')
plt.show()
```
