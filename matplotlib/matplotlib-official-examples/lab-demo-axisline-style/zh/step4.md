# 绘制图表

现在我们将使用 `np.linspace` 和 `np.sin` 来绘制图表。

```python
x = np.linspace(-0.5, 1., 100)
ax.plot(x, np.sin(x*np.pi))
```
