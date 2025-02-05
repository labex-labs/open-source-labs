# 自定义直方图

我们可以通过使用 `color`、`alpha` 和 `edgecolor` 参数来更改条形图的颜色、透明度和边缘颜色，从而自定义直方图。

```python
plt.hist(x, n_bins, color='green', alpha=0.5, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')
plt.show()
```
