# 회전된 수직선의 점을 얻는 함수 정의

원점 좌표, 선 길이 및 각도를 입력으로 받아 지정된 각도로 회전된 수직선 끝의 xy 좌표를 반환하는 함수를 정의합니다.

```python
def get_point_of_rotated_vertical(origin, line_length, degrees):
    """Return xy coordinates of the vertical line end rotated by degrees."""
    rad = np.deg2rad(-degrees)
    return [origin[0] + line_length * np.sin(rad),
            origin[1] + line_length * np.cos(rad)]
```
