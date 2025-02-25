# 注釈接続スタイルを作成する関数を定義する

軸オブジェクトと接続スタイルの2つのパラメータを受け取る関数を定義します。この関数は、2つのデータポイントをプロットし、指定された接続スタイルで注釈を作成します。

```python
def demo_con_style(ax, connectionstyle):
    x1, y1 = 0.3, 0.2
    x2, y2 = 0.8, 0.6

    ax.plot([x1, x2], [y1, y2], ".")
    ax.annotate("",
                xy=(x1, y1), xycoords='data',
                xytext=(x2, y2), textcoords='data',
                arrowprops=dict(arrowstyle="->", color="0.5",
                                shrinkA=5, shrinkB=5,
                                patchA=None, patchB=None,
                                connectionstyle=connectionstyle,
                                ),
                )

    ax.text(.05,.95, connectionstyle.replace(",", ",\n"),
            transform=ax.transAxes, ha="left", va="top")
```
