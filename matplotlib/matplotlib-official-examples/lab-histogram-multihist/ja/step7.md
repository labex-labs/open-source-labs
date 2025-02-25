# 積み重ねヒストグラムを描画する

`stacked`パラメータを`True`に設定することで、積み重ねヒストグラムを描画することができます。

```python
plt.hist(x, n_bins, color=['green', 'blue','red'], alpha=0.5, edgecolor='black', label=['Sample 1', 'Sample 2', 'Sample 3'], stacked=True)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Stacked Histogram of Random Data')
plt.legend()
plt.show()
```
