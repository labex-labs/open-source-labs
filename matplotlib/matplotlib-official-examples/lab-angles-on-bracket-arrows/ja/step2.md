# 回転させた垂直線の端点を取得する関数を定義する

原点座標、線分の長さ、角度（度単位）を入力として受け取り、指定された角度だけ回転させた垂直線の端点のxy座標を返す関数を定義します。

```python
def get_point_of_rotated_vertical(origin, line_length, degrees):
    """Return xy coordinates of the vertical line end rotated by degrees."""
    rad = np.deg2rad(-degrees)
    return [origin[0] + line_length * np.sin(rad),
            origin[1] + line_length * np.cos(rad)]
```
