# マーカーの塗りつぶしスタイル

塗りつぶされたマーカーの枠線色と塗りつぶし色は、それぞれ別々に指定できます。また、`fillstyle`を設定することで、塗りつぶされていない、完全に塗りつぶされた、または様々な方向に半分だけ塗りつぶされたスタイルに設定できます。半分だけ塗りつぶされたスタイルでは、2番目の塗りつぶし色として`markerfacecoloralt`が使用されます。次のコードは、マーカーの塗りつぶしスタイルを作成する方法を示しています。

```python
fig, ax = plt.subplots()
fig.suptitle('Marker fillstyle', fontsize=14)
fig.subplots_adjust(left=0.4)

filled_marker_style = dict(marker='o', linestyle=':', markersize=15,
                           color='darkgrey',
                           markerfacecolor='tab:blue',
                           markerfacecoloralt='lightsteelblue',
                           markeredgecolor='brown')

for y, fill_style in enumerate(Line2D.fillStyles):
    ax.text(-0.5, y, repr(fill_style), **text_style)
    ax.plot([y] * 3, fillstyle=fill_style, **filled_marker_style)
format_axes(ax)
```
