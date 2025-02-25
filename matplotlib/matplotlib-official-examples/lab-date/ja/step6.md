# 簡潔なフォーマッタを使って目盛りラベルをフォーマットする

2番目のサブプロットの目盛りラベルを、簡潔なフォーマッタを使ってフォーマットします。

```python
ax = axs[1]
ax.set_title('ConciseFormatter', loc='left', y=0.85, x=0.02, fontsize='medium')
ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(ax.xaxis.get_major_locator()))
```
