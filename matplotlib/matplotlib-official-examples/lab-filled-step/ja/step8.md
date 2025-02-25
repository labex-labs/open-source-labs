# ラベル付きのハッチ付きヒストグラムを作成する

先ほど定義した `stack_hist` 関数を使って、ラベル付きのハッチ付きヒストグラムを作成します。先ほど定義した `dict_data`、`color_cycle`、および `hist_func` を使用します。また、最初と最後のセットのみをプロットするために、`labels` を `['set 0','set 3']` に設定します。

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5), tight_layout=True, sharey=True)
dict_data = dict(zip((c['label'] for c in label_cycle), stack_data))
arts = stack_hist(ax1, dict_data, color_cycle + hatch_cycle, hist_func=hist_func)

arts = stack_hist(ax2, dict_data, color_cycle + hatch_cycle, hist_func=hist_func, labels=['set 0','set 3'])
ax1.xaxis.set_major_locator(mticker.MaxNLocator(5))
ax1.set_xlabel('counts')
ax1.set_ylabel('x')
ax2.set_ylabel('x')
```
