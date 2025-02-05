# 绘制数据

既然我们已经创建了子图，那么我们可以使用 `np.sin(x)` 来绘制数据。

```python
x = np.arange(0, 2*np.pi, 0.01)
ax0.plot(x, np.sin(x))
ax1.plot(x, np.sin(x))
```
