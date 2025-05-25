# Koch 설화 함수 정의

다음으로, Koch 설화를 생성하는 함수를 정의합니다. 이 함수는 재귀 깊이 (recursion depth) 와 스케일 팩터 (scale factor) 의 두 가지 매개변수를 사용합니다.

```python
def koch_snowflake(order, scale=10):
    """
    Koch 설화의 점 좌표를 나타내는 두 개의 리스트 x, y 를 반환합니다.

    매개변수
    ----------
    order : int
        재귀 깊이.
    scale : float
        설화의 크기 (기본 삼각형의 변 길이).
    """
    def _koch_snowflake_complex(order):
        if order == 0:
            # initial triangle
            angles = np.array([0, 120, 240]) + 90
            return scale / np.sqrt(3) * np.exp(np.deg2rad(angles) * 1j)
        else:
            ZR = 0.5 - 0.5j * np.sqrt(3) / 3

            p1 = _koch_snowflake_complex(order - 1)  # start points
            p2 = np.roll(p1, shift=-1)  # end points
            dp = p2 - p1  # connection vectors

            new_points = np.empty(len(p1) * 4, dtype=np.complex128)
            new_points[::4] = p1
            new_points[1::4] = p1 + dp / 3
            new_points[2::4] = p1 + dp * ZR
            new_points[3::4] = p1 + dp / 3 * 2
            return new_points

    points = _koch_snowflake_complex(order)
    x, y = points.real, points.imag
    return x, y
```
