# 좌표 형식 지정자 수정

이제 x 와 y 가 주어졌을 때 가장 가까운 픽셀의 이미지 "z" 값을 보고하도록 좌표 형식 지정자를 수정합니다. 이는 `~.axes.Axes.format_coord` 함수를 사용자 정의하여 수행할 수 있습니다.

```python
def format_coord(x, y):
    col = round(x)
    row = round(y)
    nrows, ncols = X.shape
    if 0 <= col < ncols and 0 <= row < nrows:
        z = X[row, col]
        return f'x={x:1.4f}, y={y:1.4f}, z={z:1.4f}'
    else:
        return f'x={x:1.4f}, y={y:1.4f}'

ax.format_coord = format_coord
```
