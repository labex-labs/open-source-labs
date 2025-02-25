# ヒストグラムをカスタマイズする

`color`、`alpha`、`edgecolor`パラメータを使って、棒グラフの色、透明度、枠線の色を変更することで、ヒストグラムをカスタマイズすることができます。

```python
plt.hist(x, n_bins, color='green', alpha=0.5, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')
plt.show()
```
