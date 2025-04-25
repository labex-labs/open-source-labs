# エラーボックス用の関数を作成する

ここでは、`make_error_boxes` という関数を作成します。この関数は、x 方向と y 方向のバーの限界で定義された四角形のパッチを作成します。

```python
def make_error_boxes(ax, xdata, ydata, xerror, yerror, facecolor='r',
                     edgecolor='none', alpha=0.5):

    # データポイントをループします。各ポイントのエラーからボックスを作成します
    errorboxes = [Rectangle((x - xe[0], y - ye[0]), xe.sum(), ye.sum())
                  for x, y, xe, ye in zip(xdata, ydata, xerror.T, yerror.T)]

    # 指定された色/透明度でパッチコレクションを作成します
    pc = PatchCollection(errorboxes, facecolor=facecolor, alpha=alpha,
                         edgecolor=edgecolor)

    # コレクションを軸に追加します
    ax.add_collection(pc)

    # エラーバーを描画します
    artists = ax.errorbar(xdata, ydata, xerr=xerror, yerr=yerror,
                          fmt='none', ecolor='k')

    return artists
```
