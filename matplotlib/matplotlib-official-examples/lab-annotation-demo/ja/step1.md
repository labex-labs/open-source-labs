# テキストポイントと注釈ポイントの指定

このポイントに注釈を付けるには、注釈ポイント `xy=(x, y)` を指定する必要があります。また、この注釈のテキストの位置について、テキストポイント `xytext=(x, y)` を指定することもできます。任意で、`xycoords` と `textcoords` のために、次の文字列のいずれかを使って `xy` と `xytext` の座標系を指定できます（デフォルトは 'data'）：

- 'figure points' : グラフの左下隅からのポイント
- 'figure pixels' : グラフの左下隅からのピクセル
- 'figure fraction' : (0, 0) はグラフの左下隅で、(1, 1) は右上隅
- 'axes points' : 軸の左下隅からのポイント
- 'axes pixels' : 軸の左下隅からのピクセル
- 'axes fraction' : (0, 0) は軸の左下隅で、(1, 1) は右上隅
- 'offset points' : xy 値からのオフセット（ポイントで）を指定
- 'offset pixels' : xy 値からのオフセット（ピクセルで）を指定
- 'data' : 軸のデータ座標系を使用

注：物理座標系（ポイントまたはピクセル）の場合、原点はグラフまたは軸の (下，左) です。

任意で、注釈ポイントに向かってテキストから矢印を引く矢印のプロパティを指定できます。これは、矢印のプロパティの辞書を与えることで行います。有効なキーは：

- `width` : 矢印の幅（ポイントで）
- `frac` : 矢印の先端が占める矢印の長さの割合
- `headwidth` : 矢印の先端の基部の幅（ポイントで）
- `shrink` : 先端と基部を注釈ポイントとテキストから何パーセント離すか
- `matplotlib.patches.polygon` の任意のキー（例えば、facecolor）

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Ellipse
from matplotlib.text import OffsetFrom

# Create our figure and data we'll use for plotting
fig, ax = plt.subplots(figsize=(4, 4))

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)

# Plot a line and add some simple annotations
line, = ax.plot(t, s)
ax.annotate('figure pixels',
            xy=(10, 10), xycoords='figure pixels')
ax.annotate('figure points',
            xy=(107, 110), xycoords='figure points',
            fontsize=12)
ax.annotate('figure fraction',
            xy=(.025,.975), xycoords='figure fraction',
            horizontalalignment='left', verticalalignment='top',
            fontsize=20)

# The following examples show off how these arrows are drawn.

ax.annotate('point offset from data',
            xy=(3, 1), xycoords='data',
            xytext=(-10, 90), textcoords='offset points',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='center', verticalalignment='bottom')

ax.annotate('axes fraction',
            xy=(2, 1), xycoords='data',
            xytext=(0.36, 0.68), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')

# You may also use negative points or pixels to specify from (right, top).
# E.g., (-10, 10) is 10 points to the left of the right side of the axes and 10
# points above the bottom

ax.annotate('pixel offset from axes fraction',
            xy=(1, 0), xycoords='axes fraction',
            xytext=(-20, 20), textcoords='offset pixels',
            horizontalalignment='right',
            verticalalignment='bottom')

ax.set(xlim=(-1, 5), ylim=(-3, 5))
```
