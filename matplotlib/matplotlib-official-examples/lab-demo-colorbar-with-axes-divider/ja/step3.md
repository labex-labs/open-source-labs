# プロットにカラーバーを追加する

次に、Matplotlib の`make_axes_locatable`関数を使って、各サブプロットにカラーバーを追加します。この関数は既存の軸を受け取り、新しい`AxesDivider`に追加して`AxesDivider`を返します。その後、`AxesDivider`の`append_axes`メソッドを使って、元の軸の特定の側（「上」、「右」、「下」、または「左」）に新しい軸を作成できます。

```python
ax1_divider = make_axes_locatable(ax1)
cax1 = ax1_divider.append_axes("right", size="7%", pad="2%")
cb1 = fig.colorbar(im1, cax=cax1)

ax2_divider = make_axes_locatable(ax2)
cax2 = ax2_divider.append_axes("top", size="7%", pad="2%")
cb2 = fig.colorbar(im2, cax=cax2, orientation="horizontal")
cax2.xaxis.set_ticks_position("top")
```
