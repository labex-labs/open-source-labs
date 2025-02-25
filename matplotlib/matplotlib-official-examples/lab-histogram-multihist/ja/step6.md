# 複数のヒストグラムを描画する

`hist`関数にデータの配列を渡すことで、同じグラフに複数のヒストグラムを描画することができます。

```python
plt.hist(x, n_bins, color='green', alpha=0.5, edgecolor='black', label=['Sample 1', 'Sample 2', 'Sample 3'])
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')
plt.legend()
plt.show()
```
