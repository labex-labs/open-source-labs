# 関数の適用

関数ができたので、これを使って注釈付きのヒートマップを作成できます。新しいデータセットを作成し、`imshow`にさらに引数を与え、注釈に整数形式を使い、いくつかの色を指定します。また、`matplotlib.ticker.FuncFormatter`を使って対角成分（すべて1）を非表示にします。

```python
data = np.random.randint(2, 100, size=(7, 7))
y = [f"Book {i}" for i in range(1, 8)]
x = [f"Store {i}" for i in list("ABCDEFG")]

fig, ax = plt.subplots()
im, _ = heatmap(data, y, x, ax=ax, vmin=0, cmap="magma_r", cbarlabel="weekly sold copies")
annotate_heatmap(im, valfmt="{x:d}", size=7, threshold=20, textcolors=("red", "white"))

def func(x, pos):
    return f"{x:.2f}".replace("0.", ".").replace("1.00", "")

annotate_heatmap(im, valfmt=matplotlib.ticker.FuncFormatter(func), size=7)
```
