# 縦積み棒グラフを作成する

異なる自然災害による損失を年間で表すために、`plt.bar`関数を使って縦積み棒グラフを作成します。データの各行を反復処理するために for ループを使い、棒グラフを描画します。

```python
n_rows = len(data)

index = np.arange(len(columns)) + 0.3
bar_width = 0.4

y_offset = np.zeros(len(columns))

cell_text = []
for row in range(n_rows):
    plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
    y_offset = y_offset + data[row]
    cell_text.append(['%1.1f' % (x / 1000.0) for x in y_offset])
```
