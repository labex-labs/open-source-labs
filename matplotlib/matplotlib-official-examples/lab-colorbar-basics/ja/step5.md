# 正と負のデータを含むプロットを作成する

正と負のデータの両方を含むプロットを作成し、`colorbar` 関数を使ってプロットにカラーバーを追加します。今回は、`vmin` と `vmax` パラメータを使ってカラーバーの最小値と最大値を指定します。

```python
# Plot both positive and negative values between +/- 1.2
pos_neg_clipped = plt.imshow(Z, cmap='RdBu', vmin=-1.2, vmax=1.2,
                             interpolation='none')

# Add minorticks on the colorbar to make it easy to read the
# values off the colorbar.
cbar = plt.colorbar(pos_neg_clipped, extend='both')
cbar.minorticks_on()
```
