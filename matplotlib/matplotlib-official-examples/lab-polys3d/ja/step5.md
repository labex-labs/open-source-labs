# 頂点と面の色を計算する

Matplotlib の`vectorize`関数と`colormaps`関数を使って、頂点と面の色を計算します。

```python
# verts[i] は、ポリゴン i を定義する (x, y) のペアのリストです。
gamma = np.vectorize(math.gamma)
verts = [polygon_under_graph(x, l**x * np.exp(-l) / gamma(x + 1))
         for l in lambdas]
facecolors = plt.colormaps['viridis_r'](np.linspace(0, 1, len(verts)))
```
