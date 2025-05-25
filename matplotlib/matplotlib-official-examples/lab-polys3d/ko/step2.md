# 그래프 아래 다각형 함수 정의

다음으로, (x, y) 선 그래프 아래 공간을 채우는 다각형을 정의하는 정점 목록을 구성하는 함수 `polygon_under_graph(x, y)`를 정의합니다. 이 함수는 x 가 오름차순이라고 가정합니다.

```python
def polygon_under_graph(x, y):
    """
    Construct the vertex list which defines the polygon filling the space under
    the (x, y) line graph. This assumes x is in ascending order.
    """
    return [(x[0], 0.), *zip(x, y), (x[-1], 0.)]
```
