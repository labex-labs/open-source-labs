# 散布図にテキストを追加する

ここでは、`offset_copy` を使用して散布図にテキストを追加します。まず、任意の座標で指定された場所に対して画面座標における指定されたオフセットでテキストを配置する変換を作成します。その後、`matplotlib.pyplot` の `text` 関数を使用してグラフにテキストを追加します。

```python
# Create the transform
trans_offset = mtransforms.offset_copy(ax.transData, fig=fig,
                                       x=0.05, y=0.10, units='inches')

# Add text to the plot
for x, y in zip(xs, ys):
    plt.text(x, y, '%d, %d' % (int(x), int(y)), transform=trans_offset)
```
