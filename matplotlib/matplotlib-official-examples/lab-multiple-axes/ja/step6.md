# アニメーション関数の定義

6 番目のステップは、アニメーション関数を定義することです。この関数はアニメーションの各フレームで呼び出され、左のサブプロット上の点の位置、右のサブプロット上のサインカーブの位置とデータ、接続パッチの位置を更新します。

```python
def animate(i):
    x = np.linspace(0, i, int(i * 25 / np.pi))
    sine.set_data(x, np.sin(x))
    x, y = np.cos(i), np.sin(i)
    point.set_data([x], [y])
    con.xy1 = x, y
    con.xy2 = i, y
    return point, sine, con
```
