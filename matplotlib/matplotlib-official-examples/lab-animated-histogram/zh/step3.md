# 创建数据和直方图

使用 NumPy 创建数据和直方图。

```python
# histogram our data with numpy
data = np.random.randn(1000)
n, _, _ = plt.hist(data, HIST_BINS, lw=1, ec="yellow", fc="green", alpha=0.5)
```
