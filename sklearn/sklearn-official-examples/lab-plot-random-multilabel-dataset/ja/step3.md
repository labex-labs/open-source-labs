# データセットをプロットする

ここでは、`plot_2d`関数を使ってランダムに生成されたマルチラベルデータセットをプロットします。2つのサブプロットを持つ図を作成し、それぞれのサブプロットに異なるパラメータ値を使って`plot_2d`関数を呼び出します。

```python
_, (ax1, ax2) = plt.subplots(1, 2, sharex="row", sharey="row", figsize=(8, 4))
plt.subplots_adjust(bottom=0.15)

p_c, p_w_c = plot_2d(ax1, n_labels=1)
ax1.set_title("n_labels=1, length=50")
ax1.set_ylabel("Feature 1 count")

plot_2d(ax2, n_labels=3)
ax2.set_title("n_labels=3, length=50")
ax2.set_xlim(left=0, auto=True)
ax2.set_ylim(bottom=0, auto=True)

plt.show()
```
