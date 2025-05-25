# 선분 생성

개별적으로 색상을 지정할 수 있도록 일련의 선분을 생성합니다. numpy 의 `concatenate` 함수를 사용하여 두 배열 `points[:-1]`과 `points[1:]`을 두 번째 축을 따라 연결합니다. 그런 다음 결과 배열을 N x 1 x 2 배열로 재구성하여 점들을 쉽게 쌓아 세그먼트를 얻을 수 있습니다. 선 집합 (line collection) 에 대한 segments 배열은 (numlines) x (points per line) x 2 (x 및 y 에 대해) 여야 합니다.

```python
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
```
