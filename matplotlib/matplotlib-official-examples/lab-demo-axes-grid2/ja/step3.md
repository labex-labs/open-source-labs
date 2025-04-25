# サンプルデータを準備する

サンプルデータを取得するために、cbook から`get_sample_data`関数を使用します。その後、グリッドに表示する画像を準備します。

```python
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
extent = (-3, 4, -4, 3)
ZS = [Z[i::3, :] for i in range(3)]
extent = extent[0], extent[1]/3., extent[2], extent[3]
```
