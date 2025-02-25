# ノッチ付きのボックスプロットの作成

次に、`boxplot()`関数を使ってノッチ付きのボックスプロットを作成します。ノッチ付きのボックスプロットを作成するために、`notch`パラメータを`True`に設定します。

```python
fig, ax2 = plt.subplots(figsize=(9, 4))
bplot2 = ax2.boxplot(all_data,
                     notch=True,  # notch shape
                     vert=True,  # vertical box alignment
                     patch_artist=True,  # fill with color
                     labels=labels)  # x-tick labels
ax2.set_title('Notched Box Plot')
```
