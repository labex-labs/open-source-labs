# 2 番目の内側のグリッドスペックにサブプロットを追加する

次に、2 番目の内側のグリッドスペックにサブプロットを追加します。`ax4`、`ax5`、`ax6`の 3 つのサブプロットを作成します。

```python
ax4 = fig.add_subplot(gs01[:, :-1])
ax5 = fig.add_subplot(gs01[:-1, -1])
ax6 = fig.add_subplot(gs01[-1, -1])
```
