# インセット軸を作成する

次に、各サブプロットにインセット軸を作成します。インセット軸を作成するには、`inset_axes()` メソッドを使用します。異なるサイズと位置の4つのインセットを作成します。

```python
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# 幅1.3インチ、高さ0.9インチのインセットを
# 既定の右上の位置に作成する
axins = inset_axes(ax, width=1.3, height=0.9)

# 親軸のバウンディングボックスの幅の30%、高さの40%のインセットを
# 左下隅 (loc=3) に作成する
axins2 = inset_axes(ax, width="30%", height="40%", loc=3)

# 2番目のサブプロットに混合仕様のインセットを作成する;
# 幅は親軸のバウンディングボックスの30%で
# 高さは1インチで左上隅 (loc=2) に作成する
axins3 = inset_axes(ax2, width="30%", height=1., loc=2)

# 右下隅 (loc=4) にボーダーパッドを1としてインセットを作成する、つまり
# 親軸に対して10ポイントのパディング (10ptが既定のフォントサイズなので) を持つ
axins4 = inset_axes(ax2, width="20%", height="20%", loc=4, borderpad=1)
```
