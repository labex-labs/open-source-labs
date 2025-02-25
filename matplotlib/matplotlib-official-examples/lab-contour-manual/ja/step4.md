# 穴のある塗りつぶされた等高線を作成する

Path クラスで説明されているように、多角形の頂点の単一のリストと頂点の種類（コードタイプ）のリストとともに、複数の塗りつぶされた等高線を指定することができます。これは、穴のある多角形に特に役立ちます。

```python
fig, ax = plt.subplots()
filled01 = [[[0, 0], [3, 0], [3, 3], [0, 3], [1, 1], [1, 2], [2, 2], [2, 1]]]
M = Path.MOVETO
L = Path.LINETO
kinds01 = [[M, L, L, L, M, L, L, L]]
cs = ContourSet(ax, [0, 1], [filled01], [kinds01], filled=True)
cbar = fig.colorbar(cs)

ax.set(xlim=(-0.5, 3.5), ylim=(-0.5, 3.5),
       title='User specified filled contours with holes')
```
