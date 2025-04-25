# 軸の範囲を設定してグラフを保存する

軸の x と y の範囲を設定し、`io.BytesIO()` と `plt.savefig()` を使ってグラフを SVG 形式のバイト文字列として保存します。

```python
ax.set_xlim(0., 1.)
ax.set_ylim(0., 1.)

f = io.BytesIO()
plt.savefig(f, format="svg")
```
