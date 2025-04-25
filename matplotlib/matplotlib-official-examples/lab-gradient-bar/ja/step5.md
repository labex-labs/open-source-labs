# グラフを作成する

これで、グラフを作成することができます。まず、グラフィックオブジェクトと軸オブジェクトを作成します。その後、軸の x 軸と y 軸の範囲を設定します。`gradient_image()`関数を使用してグラデーション背景を作成します。最後に、ランダムなデータセットを作成し、`gradient_bar()`関数を使用して棒グラフを作成します。

```python
fig, ax = plt.subplots()
ax.set(xlim=(0, 10), ylim=(0, 1))

# background image
gradient_image(ax, direction=1, extent=(0, 1, 0, 1), transform=ax.transAxes,
               cmap=plt.cm.RdYlGn, cmap_range=(0.2, 0.8), alpha=0.5)

N = 10
x = np.arange(N) + 0.15
y = np.random.rand(N)
gradient_bar(ax, x, y, width=0.7)
plt.show()
```
