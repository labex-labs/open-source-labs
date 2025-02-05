# 创建图表

接下来，我们将使用 Matplotlib 的 `subplots()` 函数创建图表，并绘制谷歌股票随时间变化的调整收盘价。

```python
fig, ax = plt.subplots()
ax.plot(r.date, r.adj_close)
```
