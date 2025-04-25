# グリッド線とラベルの追加

グラフに水平方向のグリッド線を追加し、x 軸と y 軸のラベルを設定します。

```python
for ax in axs:
    ax.yaxis.grid(True)
    ax.set_xticks([y + 1 for y in range(len(all_data))], labels=['x1', 'x2', 'x3', 'x4'])
    ax.set_xlabel('Four separate samples')
    ax.set_ylabel('Observed values')
```
