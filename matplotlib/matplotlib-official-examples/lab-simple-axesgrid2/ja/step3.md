# 画像データを読み込む

ImageGridを示すために、`cbook`からの`bivariate_normal.npy`と呼ばれるサンプル画像データを使用します。`cbook`の`get_sample_data`関数を使用して画像データを読み込みます。

```python
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
im1 = Z
im2 = Z[:, :10]
im3 = Z[:, 10:]
vmin, vmax = Z.min(), Z.max()
```
