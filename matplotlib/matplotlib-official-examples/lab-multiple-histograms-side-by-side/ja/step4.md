# ヒストグラムを描画する

これで、描画に必要な量を計算したので、ヒストグラムを作成できます。各ヒストグラムに対して水平バーを描画するために`barh`メソッドを使用します。

```python
# すべてのヒストグラムのビンの境界は同じです
bin_edges = np.linspace(hist_range[0], hist_range[1], number_of_bins + 1)
heights = np.diff(bin_edges)
centers = bin_edges[:-1] + heights / 2

# 各ヒストグラムをループして描画します
fig, ax = plt.subplots()
for x_loc, binned_data in zip(x_locations, binned_data_sets):
    lefts = x_loc - 0.5 * binned_data
    ax.barh(centers, binned_data, height=heights, left=lefts)

ax.set_xticks(x_locations, labels)
ax.set_ylabel("Data values")
ax.set_xlabel("Data sets")
```
