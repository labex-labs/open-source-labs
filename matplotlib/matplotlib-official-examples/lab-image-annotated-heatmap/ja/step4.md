# より複雑なヒートマップの例

以下では、以前に作成した関数の汎用性を、さまざまなケースで適用し、さまざまな引数を使って示します。

```python
np.random.seed(19680801)

fig, ((ax, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(8, 6))

# 上の例を、異なるフォントサイズとカラーマップで再現します。

im, _ = heatmap(harvest, vegetables, farmers, ax=ax, cmap="Wistia", cbarlabel="harvest [t/year]")
annotate_heatmap(im, valfmt="{x:.1f}", size=7)

# 時には、データ自体がカテゴリである場合もあります。ここでは、`matplotlib.colors.BoundaryNorm`を使ってデータをクラスに分け、これを使ってプロットを着色するだけでなく、クラスの配列からクラスラベルも取得します。

data = np.random.randn(6, 6)
y = [f"Prod. {i}" for i in range(10, 70, 10)]
x = [f"Cycle {i}" for i in range(1, 7)]

qrates = list("ABCDEFG")
norm = matplotlib.colors.BoundaryNorm(np.linspace(-3.5, 3.5, 8), 7)
fmt = matplotlib.ticker.FuncFormatter(lambda x, pos: qrates[::-1][norm(x)])

im, _ = heatmap(data, y, x, ax=ax3, cmap=mpl.colormaps["PiYG"].resampled(7), norm=norm, cbar_kw=dict(ticks=np.arange(-3, 4), format=fmt), cbarlabel="Quality Rating")
annotate_heatmap(im, valfmt=fmt, size=9, fontweight="bold", threshold=-1, textcolors=("red", "black"))

# 相関行列をきれいにプロットできます。これは-1と1で制限されるため、これらをvminとvmaxとして使います。

corr_matrix = np.corrcoef(harvest)
im, _ = heatmap(corr_matrix, vegetables, vegetables, ax=ax4, cmap="PuOr", vmin=-1, vmax=1, cbarlabel="correlation coeff.")
annotate_heatmap(im, valfmt=matplotlib.ticker.FuncFormatter(func), size=7)

plt.tight_layout()
plt.show()
```
