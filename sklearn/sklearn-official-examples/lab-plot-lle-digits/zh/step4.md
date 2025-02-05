# 绘制结果

我们将绘制每种方法给出的最终投影。

```python
for name in timing:
    title = f"{name} (时间 {timing[name]:.3f}秒)"
    plot_embedding(projections[name], title)

plt.show()
```
