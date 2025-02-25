# ハッチ付きのヒストグラムを作成する

先ほど定義した `stack_hist` 関数を使って、ハッチ付きのヒストグラムを作成します。先ほど定義した `stack_data`、`color_cycle`、および `hist_func` を使用します。また、`plot_kwargs` には端の色と方向を含めるように設定します。

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5), tight_layout=True)
arts = stack_hist(ax1, stack_data, color_cycle + label_cycle + hatch_cycle, hist_func=hist_func)

arts = stack_hist(ax2, stack_data, color_cycle, hist_func=hist_func, plot_kwargs=dict(edgecolor='w', orientation='h'))
ax1.set_ylabel('counts')
ax1.set_xlabel('x')
ax2.set_xlabel('counts')
ax2.set_ylabel('x')
```
