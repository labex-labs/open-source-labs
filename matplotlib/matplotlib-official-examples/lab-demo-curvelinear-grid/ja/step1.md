# カスタム変換用のグリッド

まず、`GridHelperCurveLinear` を使用してカスタム グリッドと目盛り線を作成します。カスタム変換は、グリッドと目盛り線に適用されます。次のコードはこのプロセスを示しています。

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.projections import PolarAxes
from matplotlib.transforms import Affine2D
from mpl_toolkits.axisartist import Axes, HostAxes, angle_helper
from mpl_toolkits.axisartist.grid_helper_curvelinear import GridHelperCurveLinear

def curvelinear_test1(fig):
    # カスタム変換を定義する
    def tr(x, y):
        return x, y - x
    def inv_tr(x, y):
        return x, y + x

    # GridHelperCurveLinear オブジェクトを作成する
    grid_helper = GridHelperCurveLinear((tr, inv_tr))

    # カスタム グリッドと目盛り線付きのサブプロットを作成する
    ax1 = fig.add_subplot(1, 2, 1, axes_class=Axes, grid_helper=grid_helper)

    # サブプロットにいくつかの点をプロットする
    xx, yy = tr(np.array([3, 6]), np.array([5, 10]))
    ax1.plot(xx, yy)

    # サブプロットのアスペクト比と範囲を設定する
    ax1.set_aspect(1)
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)

    # 浮動軸とグリッド線を追加する
    ax1.axis["t"] = ax1.new_floating_axis(0, 3)
    ax1.axis["t2"] = ax1.new_floating_axis(1, 7)
    ax1.grid(True, zorder=0)

fig = plt.figure(figsize=(7, 4))
curvelinear_test1(fig)
plt.show()
```
