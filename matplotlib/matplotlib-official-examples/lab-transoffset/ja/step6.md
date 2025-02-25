# 極座標グラフにテキストを追加する

最後に、`offset_copy` と `matplotlib.pyplot` の `text` 関数を使用して極座標グラフにテキストを追加します。

```python
# Create the transform
trans_offset = mtransforms.offset_copy(ax.transData, fig=fig,
                                       y=6, units='dots')

# Add text to the plot
for x, y in zip(xs, ys):
    plt.text(x, y, '%d, %d' % (int(x), int(y)),
             transform=trans_offset,
             horizontalalignment='center',
             verticalalignment='bottom')
```
