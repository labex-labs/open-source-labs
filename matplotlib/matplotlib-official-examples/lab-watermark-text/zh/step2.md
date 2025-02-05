# 生成数据

让我们生成一些随机数据用于绘图。

```python
# 固定随机种子以确保可重复性
np.random.seed(19680801)

fig, ax = plt.subplots()
ax.plot(np.random.rand(20), '-o', ms=20, lw=2, alpha=0.7, mfc='orange')
ax.grid()
```
