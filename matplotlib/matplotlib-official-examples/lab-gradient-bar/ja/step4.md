# グラデーションバー関数を定義する

次に、グラデーションバーを作成する関数を定義する必要があります。この関数は、軸オブジェクト、バーの x 座標と y 座標、バーの幅、およびバーの下端位置を受け取ります。その後、関数は各バーに対してグラデーション画像を作成して返します。

```python
def gradient_bar(ax, x, y, width=0.5, bottom=0):
    for left, top in zip(x, y):
        right = left + width
        gradient_image(ax, extent=(left, right, bottom, top),
                       cmap=plt.cm.Blues_r, cmap_range=(0, 0.8))
```
