# 创建绘图

在这一步中，我们将使用上一步创建的掩码数组来创建绘图。我们将分别绘制每个掩码数组，并为每个数组使用不同的颜色。

```python
fig, ax = plt.subplots()
ax.plot(t, smiddle, t, slower, t, supper)
plt.show()
```
