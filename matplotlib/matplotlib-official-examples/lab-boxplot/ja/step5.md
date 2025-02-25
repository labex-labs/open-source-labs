# ボックスプロットのスタイルをカスタマイズする

`boxplot()` 関数に用意されているさまざまなキーワード引数を使って、ボックスプロットのスタイルをカスタマイズすることもできます。たとえば、`boxprops` を設定することでボックスの色と線のスタイルを変更できます。また、それぞれ `medianprops`、`meanprops`、`meanlineprops` を設定することで、中央値、平均値、平均値の線のスタイルを変更できます。

```python
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(8, 8), sharey=True)
axs[0, 0].boxplot(data, labels=labels)
axs[0, 0].set_title('Default')

boxprops = dict(linestyle='--', linewidth=2, color='red')
axs[0, 1].boxplot(data, labels=labels, boxprops=boxprops)
axs[0, 1].set_title('Custom Box')

medianprops = dict(linestyle='-', linewidth=2, color='blue')
meanprops = dict(marker='D', markeredgecolor='black', markerfacecolor='green')
meanlineprops = dict(linestyle='--', linewidth=2, color='red')
axs[1, 0].boxplot(data, labels=labels, medianprops=medianprops, meanprops=meanprops, meanline=True, meanlineprops=meanlineprops)
axs[1, 0].set_title('Custom Median, Mean, and Mean Line')

flierprops = dict(marker='o', markerfacecolor='red', markersize=8, markeredgecolor='none')
axs[1, 1].boxplot(data, labels=labels, flierprops=flierprops)
axs[1, 1].set_title('Custom Outliers')

plt.show()
```
