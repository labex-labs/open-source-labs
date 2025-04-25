# プロット用の量を計算する

ヒストグラムを作成する前に、プロット用のいくつかの量を計算する必要があります。データセットの範囲、ビン分割されたデータセット、最大ビン値、および各ヒストグラムの x 座標を計算します。

```python
hist_range = (np.min(data_sets), np.max(data_sets))
number_of_bins = 20
binned_data_sets = [
    np.histogram(d, range=hist_range, bins=number_of_bins)[0]
    for d in data_sets
]
binned_maximums = np.max(binned_data_sets, axis=1)
x_locations = np.arange(0, sum(binned_maximums), np.max(binned_maximums))
```
