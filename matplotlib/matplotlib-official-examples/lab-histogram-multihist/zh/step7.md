# 绘制堆叠直方图

通过将 `stacked` 参数设置为 `True`，我们可以绘制堆叠直方图。

```python
plt.hist(x, n_bins, color=['green', 'blue','red'], alpha=0.5, edgecolor='black', label=['Sample 1', 'Sample 2', 'Sample 3'], stacked=True)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Stacked Histogram of Random Data')
plt.legend()
plt.show()
```
