# キバープロットを作成する

矢印のグリッドと方向が定義されたので、キバープロットを作成できます。この例では、Matplotlibの`quiver`関数を使ってプロットを作成します。`length`パラメータは矢印の長さを設定し、`normalize`パラメータは矢印を長さ1に正規化します。

```python
ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)
```
