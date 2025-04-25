# 初期化関数を定義する

グラフの初期状態を設定する初期化関数を定義する必要があります。この関数では、y 軸の範囲を設定し、線オブジェクトのデータをクリアします。

```python
def init():
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 1)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,
```
