# 绘制多个直方图

通过将数据数组传递给 `hist` 函数，我们可以在同一图表上绘制多个直方图。

```python
plt.hist(x, n_bins, color='green', alpha=0.5, edgecolor='black', label=['Sample 1', 'Sample 2', 'Sample 3'])
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')
plt.legend()
plt.show()
```

需要说明的是，你提供的代码中 `label` 参数使用方式有误，`label` 应该是为每个直方图单独设置标签，而不是作为一个列表整体传入，正确的用法类似这样：

```python
plt.hist(x[:, 0], n_bins, color='green', alpha=0.5, edgecolor='black', label='Sample 1')
plt.hist(x[:, 1], n_bins, color='blue', alpha=0.5, edgecolor='black', label='Sample 2')
plt.hist(x[:, 2], n_bins, color='red', alpha=0.5, edgecolor='black', label='Sample 3')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')
plt.legend()
plt.show()
```
