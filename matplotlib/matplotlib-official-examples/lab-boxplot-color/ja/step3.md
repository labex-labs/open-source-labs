# 矩形のボックスプロットの作成

次に、Matplotlib の`boxplot()`関数を使って矩形のボックスプロットを作成します。ボックスを色で塗りつぶすために、`patch_artist`パラメータを`True`に設定します。

```python
fig, ax1 = plt.subplots(figsize=(9, 4))
bplot1 = ax1.boxplot(all_data,
                     vert=True,  # vertical box alignment
                     patch_artist=True,  # fill with color
                     labels=labels)  # x-tick labels
ax1.set_title('Rectangular Box Plot')
```
