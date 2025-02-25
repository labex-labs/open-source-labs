# ポリゴンを作成してプロットに追加する

Matplotlibの`PolyCollection`関数を使ってポリゴンを作成し、それらをプロットに追加します。

```python
poly = PolyCollection(verts, facecolors=facecolors, alpha=.7)
ax.add_collection3d(poly, zs=lambdas, zdir='y')
```
