# サブプロットをカスタマイズする

下部のサブプロットの背景色を黒に設定し、x軸の目盛りを設定し、各サブプロットにタイトルを追加することで、サブプロットをカスタマイズします。

```python
axs[1, icol].set_facecolor('k')
axs[1, icol].xaxis.set_ticks(np.arange(0, 10, 2))
axs[0, icol].set_title(f'line widths (pts): {lwx:g}, {lwy:g}',
                       fontsize='medium')
```
