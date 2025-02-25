# デフォルトのフォーマッタを使って目盛りラベルをフォーマットする

最初のサブプロットの目盛りラベルを、デフォルトのフォーマッタを使ってフォーマットします。

```python
ax = axs[0]
ax.set_title('DefaultFormatter', loc='left', y=0.85, x=0.02, fontsize='medium')
ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 7)))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
```
