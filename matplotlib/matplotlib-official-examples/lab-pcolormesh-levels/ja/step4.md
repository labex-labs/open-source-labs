# 規範を使ったレベルの作成

`.axes.Axes.pcolor`、`.axes.Axes.pcolormesh`、`.axes.Axes.imshow`タイプのプロットにおいて、Normalization と Colormap インスタンスを組み合わせて「レベル」を描画する方法を示します。これは、contour/contourf のレベルキーワード引数と同じように行います。

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

# 解像度を上げるためにこれらを小さくします
dx, dy = 0.05, 0.05

# x と y の境界のための 2 つの 2 次元グリッドを生成します
y, x = np.mgrid[slice(1, 5 + dy, dy),
                slice(1, 5 + dx, dx)]

z = np.sin(x)**10 + np.cos(10 + y*x) * np.cos(x)

# x と y は境界なので、z はそれらの境界の「内側」の値でなければなりません。
# したがって、z 配列から最後の値を削除します。
z = z[:-1, :-1]
levels = MaxNLocator(nbins=15).tick_values(z.min(), z.max())


# 望ましいカラーマップ、適切なレベルを選び、データ値を受け取り、それらをレベルに変換する
# 正規化インスタンスを定義します。
cmap = plt.colormaps['PiYG']
norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

fig, (ax0, ax1) = plt.subplots(nrows=2)

im = ax0.pcolormesh(x, y, z, cmap=cmap, norm=norm)
fig.colorbar(im, ax=ax0)
ax0.set_title('pcolormesh with levels')


# コントアは「点」ベースのプロットなので、境界を点の中心に変換します
cf = ax1.contourf(x[:-1, :-1] + dx/2.,
                  y[:-1, :-1] + dy/2., z, levels=levels,
                  cmap=cmap)
fig.colorbar(cf, ax=ax1)
ax1.set_title('contourf with levels')

# サブプロット間の間隔を調整して、`ax1`のタイトルと `ax0` の目盛りラベルが
# 重ならないようにします
fig.tight_layout()

plt.show()
```
