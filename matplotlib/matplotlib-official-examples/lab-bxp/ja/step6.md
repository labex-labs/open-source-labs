# 異なる要素の表示をカスタマイズする

`bxp()` 関数の様々なパラメータを使用して、ボックスプロットの異なる要素の表示をカスタマイズすることができます。この例では、ボックス、中央値、外れ値、平均点、および平均線をどのようにカスタマイズするかを示します。

```python
# Customize the display of different elements
boxprops = dict(linestyle='--', linewidth=3, color='darkgoldenrod')
flierprops = dict(marker='o', markerfacecolor='green', markersize=12, linestyle='none')
medianprops = dict(linestyle='-.', linewidth=2.5, color='firebrick')
meanpointprops = dict(marker='D', markeredgecolor='black', markerfacecolor='firebrick')
meanlineprops = dict(linestyle='--', linewidth=2.5, color='purple')

plt.bxp(stats, boxprops=boxprops, flierprops=flierprops, medianprops=medianprops, meanprops=meanpointprops, meanline=True, showmeans=True)
plt.show()
```
