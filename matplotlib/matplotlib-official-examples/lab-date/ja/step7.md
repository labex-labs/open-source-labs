# 手動で目盛りラベルをフォーマットする

`datetime.date.strftime` に記載されているフォーマット文字列で日付をフォーマットするために、`DateFormatter` を使って3番目のサブプロットの目盛りラベルを手動でフォーマットします。

```python
ax = axs[2]
ax.set_title('Manual DateFormatter', loc='left', y=0.85, x=0.02, fontsize='medium')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b'))
for label in ax.get_xticklabels(which='major'):
    label.set(rotation=30, horizontalalignment='right')
```
