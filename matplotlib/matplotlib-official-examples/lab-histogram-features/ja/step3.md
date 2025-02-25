# ヒストグラムを作成する

このステップでは、matplotlibを使ってヒストグラムを作成します。ビンの数を50に設定し、密度パラメータを有効にしてビンの高さを正規化し、ヒストグラムの積分が1になるようにします。

```python
num_bins = 50
fig, ax = plt.subplots()
n, bins, patches = ax.hist(x, num_bins, density=True)
```
