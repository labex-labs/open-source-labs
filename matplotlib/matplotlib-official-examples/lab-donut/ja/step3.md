# 円の作成

`make_circle()`関数を使って円を作成します。この関数は円の半径を入力として受け取り、円の x 座標と y 座標を返します。

```python
def make_circle(r):
    t = np.arange(0, np.pi * 2.0, 0.01)
    t = t.reshape((len(t), 1))
    x = r * np.cos(t)
    y = r * np.sin(t)
    return np.hstack((x, y))
```
