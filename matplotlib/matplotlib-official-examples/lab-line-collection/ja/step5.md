# 値に色をマッピングする

`ScalarMappable.set_array`関数を使って、値の配列を色にマッピングすることもできます。新しいデータセットと新しい`LineCollection`オブジェクトを作成し、`array`パラメータを`x`値に設定します。その後、`Figure`オブジェクトの`colorbar`メソッドを使って、プロットにカラーバーを追加します。

```python
N = 50
x = np.arange(N)
ys = [x + i for i in x]
segs = [np.column_stack([x, y]) for y in ys]

fig, ax = plt.subplots()
ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(np.min(ys), np.max(ys))

line_segments = LineCollection(segs, array=x,
                               linewidths=(0.5, 1, 1.5, 2),
                               linestyles='solid')
ax.add_collection(line_segments)
axcb = fig.colorbar(line_segments)
axcb.set_label('Line Number')
ax.set_title('Line Collection with mapped colors')
plt.sci(line_segments)
plt.show()
```
