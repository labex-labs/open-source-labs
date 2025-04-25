# ヒストグラムを作成する

このステップでは、matplotlib を使ってヒストグラムを作成します。ビンの数を 50 に設定し、密度パラメータを有効にしてビンの高さを正規化し、ヒストグラムの積分が 1 になるようにします。

```python
num_bins = 50
fig, ax = plt.subplots()
n, bins, patches = ax.hist(x, num_bins, density=True)
```
