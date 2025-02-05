# 创建第二个图表

接下来，我们将创建第二个图表。我们将再次使用 `subplot`，但这次我们会将 `sharex` 属性设置为第一个图表（`ax1`）。这确保第二个图表将与第一个图表共享相同的 x 轴。

```python
ax2 = plt.subplot(212, sharex=ax1)
ax2.plot(t, np.sin(4*np.pi*t))
```
