# グラフにテキストボックスを追加する

最後に、`matplotlib.pyplot.text()` を使用してグラフにテキストボックスを追加します。軸座標でテキストボックスの位置を指定し、`bbox` パラメータを使用してボックスのプロパティを追加します。

```python
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)
```
