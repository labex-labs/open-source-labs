# 变化的线宽

在这一步中，我们将创建一个具有变化线宽的流线图。`linewidth` 参数控制流线的宽度。在这里，我们使用之前计算的 `speed` 数组来改变线宽。

```python
lw = 5*speed / speed.max()
plt.streamplot(X, Y, U, V, density=0.6, color='k', linewidth=lw)
plt.title('Varying Line Width')
plt.show()
```
