# 画像をプロットする関数を作成する

このステップでは、画像、プロット軸、および変換を入力として受け取る関数を定義します。この関数は、指定された変換で画像をプロット軸に表示します。また、画像の意図された範囲を示すために、画像の周りに黄色の矩形を表示します。

```python
def do_plot(ax, Z, transform):
    im = ax.imshow(Z, interpolation='none',
                   origin='lower',
                   extent=[-2, 4, -3, 2], clip_on=True)

    trans_data = transform + ax.transData
    im.set_transform(trans_data)

    # display intended extent of the image
    x1, x2, y1, y2 = im.get_extent()
    ax.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1], "y--",
            transform=trans_data)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-4, 4)
```
