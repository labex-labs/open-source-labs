# 创建绘图

现在我们将使用 `matplotlib.pyplot` 创建绘图。我们将绘制正弦波，并在 y = 0 处添加一条水平线。

```python
fig, ax = plt.subplots()

ax.plot(t, s, color='black')
ax.axhline(0, color='black')
```
