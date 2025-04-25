# 内側のグリッドスペックにサブプロットを追加する

次に、内側のグリッドスペックにサブプロットを追加します。`ax1`、`ax2`、`ax3`の 3 つのサブプロットを作成します。

```python
ax1 = fig.add_subplot(gs00[:-1, :])
ax2 = fig.add_subplot(gs00[-1, :-1])
ax3 = fig.add_subplot(gs00[-1, -1])
```
