# 등고선 및 다각형 정의

다음 단계는 등고선과 다각형을 정의하는 것입니다. 이 예제에서는 두 레벨 사이의 선과 채워진 등고선이 있습니다.

```python
# 각 레벨에 대한 등고선은 다각형의 목록/튜플입니다.
lines0 = [[[0, 0], [0, 4]]]
lines1 = [[[2, 0], [1, 2], [1, 3]]]
lines2 = [[[3, 0], [3, 2]], [[3, 3], [3, 4]]]  # Note two lines.

# 두 레벨 사이의 채워진 등고선도 다각형의 목록/튜플입니다.
# 점은 시계 방향 또는 반시계 방향으로 정렬될 수 있습니다.
filled01 = [[[0, 0], [0, 4], [1, 3], [1, 2], [2, 0]]]
filled12 = [[[2, 0], [3, 0], [3, 2], [1, 3], [1, 2]],   # Note two polygons.
            [[1, 4], [3, 4], [3, 3]]]
```
