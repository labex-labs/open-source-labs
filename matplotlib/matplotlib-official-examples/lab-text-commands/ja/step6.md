# グラフにテキストを追加する

`ax.text()` 関数を使ってグラフにテキストを追加できます。この関数は3つの引数を取ります：x座標、y座標、およびテキスト文字列。`style`、`bbox`、および`fontsize` 引数を使って、テキストのスタイルをカスタマイズできます。

```python
ax.text(3, 8, 'boxed italics text in data coords', style='italic',
        bbox={'facecolor':'red', 'alpha': 0.5, 'pad': 10})

ax.text(2, 6, r'an equation: $E=mc^2$', fontsize=15)

ax.text(3, 2, 'Unicode: Institut f\374r Festk\366rperphysik')

ax.text(0.95, 0.01, 'colored text in axes coords',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='green', fontsize=15)
```
